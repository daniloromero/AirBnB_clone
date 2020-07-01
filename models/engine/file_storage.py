#!/usr/bin/python3
"""FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances"""
import json
import os


class FileStorage():
    """ Class   """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name.id """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serialization method to json file """
        jdic = {}
        for k, v in self.__objects.items():
            jdic[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as jfile:
            json.dump(jdic, jfile)

    def reload(self):
        """ Deserialization method from json file"""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, 'r', encoding="utf-8") as jfile:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            dict_obj = json.load(jfile)
            for k, v in dict_obj.items():
                cls = v["__class__"]
                obj = eval(cls + "(**v)")
                self.__objects[k] = obj
