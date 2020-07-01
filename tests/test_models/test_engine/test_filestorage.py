#!/usr/bin/python3
""" Unittest for FileStorage class"""
from datetime import datetime
import io
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from os import path, remove
import unittest


class Test_all(unittest.TestCase):
    """ Test for the all method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_all_empty(self):
        """ Test Empty Dictionary """
        self.assertEqual(storage.all(), {})

    def test_basemodel(self):
        """ Test with basemodel object """
        b1 = BaseModel()
        name = b1.__class__.__name__ + '.' + b1.id
        dic = {name: b1}
        self.assertEqual(storage.all(), dic)
