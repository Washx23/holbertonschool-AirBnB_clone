#!/usr/bin/python3
"""
testing class base
"""

import pep8
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """class for testing class base model"""

    @classmethod
    def setUpClass(cls):
        """set class"""
        cls.my_model = BaseModel()

    def setUp(self):
        """set attr"""
        self.model_dict = self.my_model.to_dict()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_update(self):
        """test update date"""
        updatte_old = self.my_model.updated_at
        self.my_model.save()
        update_new = self.my_model.updated_at
        self.assertNotEqual(updatte_old, update_new)

    def test_to_dict(self):
        """test_to_dict"""
        self.assertEqual(type(self.model_dict), dict)
        self.assertTrue(isinstance(self.model_dict['created_at'], str))
        self.assertTrue(isinstance(self.model_dict['updated_at'], str))

    def test_create_base(self):
        """test instance class BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.update_at), datetime)

        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.assertIn("name", self.my_model.to_dict())
        self.assertIn("my_number", self.my_model.to_dict())
        model_dict = self.my_model.to_dict()
        self.assertEqual(model_dict["my_number"], 89)
        self.assertEqual(model_dict["name"], "My First Model")

    def test_create_kwargs(self):
        """create class from dictionary"""
        kwargs_model = BaseModel(**self.model_dict)
        self.assertIsInstance(kwargs_model, BaseModel)

    def test_pop8(self):
        """PEP8 Compliance Test"""
        style = pep8.StyleGuide()
        filenames = [
            "./models/engine/file_storage.py",
            "./models/amenity.py",
            "./models/city.py",
            "./models/place.py",
            "./models/state.py",
            "./models/base_model.py",
            "./models/__init__.py",
            "./models/user.py"
        ]
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
