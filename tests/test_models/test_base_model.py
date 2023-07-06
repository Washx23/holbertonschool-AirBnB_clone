#!/usr/bin/python3
"""
testing class base
"""

import pep8
import unittest
import os
from models import base_model
from datetime import datetime
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class base model"""

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = BaseModel()

    def setUp(self):
        """ set attr """
        self.dict = self.my_model.to_dict()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(base_model.__doc__)

    def test_update(self):
        """ test update date """
        update_old = self.my_model.updated_at
        self.my_model.save()
        update_new = self.my_model.updated_at
        self.assertTrue(update_old != update_new)

    def test_to_dict(self):
        """test_to_dict """
        bm = BaseModel()
        dic = bm.to_dict()
        self.assertEqual(type(dic), dict)
        self.assertTrue(type(dic['created_at']) is str)
        self.assertTrue(type(dic['updated_at']) is str)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_create_base(self):
        """test instance class BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)

        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.assertIn("name", self.my_model.to_dict())
        self.assertIn("my_number", self.my_model.to_dict())
        self.dict = self.my_model.to_dict()
        self.assertEqual(self.dict["my_number"], 89)
        self.assertEqual(self.dict["name"], "My First Model")

    def test_create_kwargs(self):
        """ create class from dictionary """
        self.kwargs = BaseModel(self.dict)
        self.assertIsInstance(self.kwargs, BaseModel)

    def test_pep8(self):
        style = pep8.StyleGuide()
        filenames = ["./models/engine/file_storage.py"]
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0)
        filenames = [
                "./models/amenity.py",
                "./models/city.py",
                "./models/place.py",
                "./models/state.py",
                "./models/base_model.py",
                "./models/__init__.py",
                "./models/review.py",
                "./models/user.py"]
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0)