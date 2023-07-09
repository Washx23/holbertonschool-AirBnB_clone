#!/usr/bin/python3
""" test module file storage """

import json
import unittest
import os
import models
from os import remove
from models import base_model
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class test_file_storage(unittest.TestCase):
    """ test class file storage """

    def setUp(self):
        """ set instance class """
        self.my_model = BaseModel()
        self.storage = file_storage.FileStorage()

    def test_docmodule(self):
        """ checking doc module """
        self.assertIsNotNone(file_storage.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_json(self):
        """Check file json"""
        with open("file.json") as f:
            self.assertGreater(len(f.read()), 0)

    def test_reload(self):
        """ test reload from json """
        self.my_model.name = "My_first_model"
        self.my_model.my_number = 89
        name = str(self.my_model.__class__.__name__)
        key = name + "." + str(self.my_model.id)
        self.my_model.save()
        self.storage.reload()
        objs = self.storage.all()
        self.assertIsNotNone(objs[key])
        self.obj_reload = objs[key]
        self.assertTrue(self.my_model.__dict__ == self.obj_reload.__dict__)
        self.assertTrue(self.my_model is not self.obj_reload)
        self.assertIsInstance(self.obj_reload, BaseModel)
        self.assertTrue(self.storage.all(), "My_first_model")

    def test_inst(self):
        """ test instance """
        i = FileStorage()
        self.assertEqual(i.path(), "file.json")
        bm = BaseModel()
        i.new(bm)
        self.assertGreater(len(i.all()), 0)

    def setUp(self):
        """ set attr """
        print()