#!/usr/bin/env python3
""" AirBnB Console """
import cmd
import sys
import models
import shlex
from models.engine.file_storage import FileStorage
from models.user import User
from datetime import datetime
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ class to read a command """
    prompt = '(hbnb) '

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
        tok = args.split()
        if tok[0] in self.classes:
            new_inst = eval("{}()".format(tokens[0]))
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
            if tok[0] in self.classes:
                if len(tok) > 1:
                    key = tok[0] + "." + tok[1]
                    if key in models.storage.all():
                        print(models.storage.all()[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesen't exsit **")
        except:
            print("** instance id missing **")

    def do_destroy(self, args):
        """ deletes an instance """
        tok = args.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesen't exist **")
            return
        elif len(tok) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + "." + args[1]
                storage.all().pop()
                storage.save()
            except:
                print("** no instance found **")
    
    def do_all(self, args):
        """ prints an strig representation of instances """
            





















if __name__ == '__main__':
    HBNBCommand().cmdloop()
