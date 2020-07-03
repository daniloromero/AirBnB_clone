#!/usr/bin/env python3
""" AirBnB Console """
import cmd
import sys
import models
from models.engine.file_storage import FileStorage
from models.user import User
from datetime import datetime
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ class to read a command """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User,
               "Place": Place, "State": State, "City": City,
               "Amenity": Amenity, "Review": Review}

    def emptyline(self):
        """ in case there is an empty line """
        pass

    def do_quit(self, args):
        """ quit command """
        return (True)

    def do_EOF(self, args):
        """ EOF command """
        print()
        return (True)

    def do_create(self, args):
        """ creates a new instance of base models """
        if not args:
            print("** class name missing **")
            return
        elif args in HBNBCommand.classes:
                new_inst = HBNBCommand.classes.get(args)()
                new_inst.save()
                print("{}".format(new_inst.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ prints the string representation of an instance """
        tok = args.split()
        try:
            if len(tok) == 0:
                print("** class name missing **")
                return
            if tok[0] in HBNBCommand.classes:
                if len(tok) > 1:
                    key = tok[0] + "." + tok[1]
                    if key in models.storage.all():
                        print(models.storage.all()[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except:
            print("** instance id missing **")

    def do_destroy(self, args):
        """ deletes an instance """
        tok = args.split(" ")
        if not args:
            print("** class name missing **")
            return
        elif tok[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(tok) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = tok[0] + "." + tok[1]
                storage.all().pop(key)
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, args):
        """ prints string representation off all instnaces """
        inst = []
        if not args:
            inst = list(storage.all().values())
            print(list(map(lambda x: str(x), inst)))
        elif args in HBNBCommand.classes:
            inst = list(storage.all().values())
            inst = filter(lambda x: type(x) is
                          HBNBCommand.classes.get(args), inst)
            print(list(map(lambda x: str(x), inst)))
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ will update an instance """
        tok = args.split(" ")
        if not args:
            print("** class name missing **")
        elif tok[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(tok) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(tok[0], tok[1])
              not in storage.all().keys()):
            print("** no instance found **")
        elif len(tok) == 2:
            print("** attribute name missing **")
        elif len(tok) == 3:
            print("** value missing **")
        else:
            inst = storage.all()
            key = "{}.{}".format(tok[0], tok[1])
            if key in inst.keys():
                atr = getattr(inst[key], tok[2], "")
                setattr(inst[key], tok[2], type(atr)(tok[3]))
                inst[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
