#!/usr/bin/python3
"""Unittest module for BaseModel class"""
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from os import path, remove
import json
from datetime import datetime
from uuid import uuid4
import unittest


class TestBaseModel(unittest.TestCase):
    """ Test cases for Basemodel class"""

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
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertIsInstance(bm1, BaseModel)

    def test_uniq_id(self):
        """Tests unique user ids."""

        l = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(l)), len(l))

    def test_kwargs_instantiation(self):
        """Tests instantiation with **kwargs."""

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

if __name__ == '__main__':
    unittest.main()
