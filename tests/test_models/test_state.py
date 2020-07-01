#!/usr/bin/python3
"""Unittest module for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import path, remove
import json
from models import storage
from datetime import datetime
from uuid import uuid4


class TestState(unittest.TestCase):
    """ Test cases for State class"""

    def setUp(self):
        """ Set up for all methods """
        pass

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_instance_creation_no_arg(self):
        """ No arguments """
        ct1 = State()
        self.assertTrue(hasattr(ct1, "id"))
        self.assertTrue(hasattr(ct1, "created_at"))
        self.assertTrue(hasattr(ct1, "updated_at"))
        self.assertIsInstance(ct1, State)
        self.assertEqual(type(ct1.id), str)
        self.assertEqual(type(ct1.created_at), datetime)
        self.assertEqual(type(ct1.updated_at), datetime)
    def test_uniq_id(self):
        """Tests unique user ids."""

        l = [State().id for i in range(1000)]
        self.assertEqual(len(set(l)), len(l))

    def test_kwargs_instantiation(self):
        """Tests instantiation with **kwargs."""

        my_model = State()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = State(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

if __name__ == "__main__":
    unittest.main()
