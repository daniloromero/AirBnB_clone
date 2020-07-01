#!/usr/bin/python3
""" test module for the console """
import unittest
import pep8
import tests
import json
import console
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class Documnetaion_Test(unittest.TestCase):
    """ will check for the console docs """
    def test_pep8(self):
        """ will check the console's pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0)

    def test_docstring(self):
        """ check for docstrings """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)


class TestConsole(unittest.TestCase):
    """ test for the console """

    @classmethod
    def setupClass(cls):
        """ will create an instance before the tests """
        cls.test_console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """ deltes an instance """
        del cls.test_console

    def tearDown(self):
        """ deletes the file after the test """
        try:
            os.remove("file.json")
        except:
            pass

    def test_emptyline(self):
        """ Test empty line function """
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("\n")
            self.assertEqual('', f.getvalue())

if __name__ == "__main__":
    unittest.main()
