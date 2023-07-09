#!/usr/bin/python3
"""
testing class console
"""

import pep8
import unittest
import console
from console import HBNBCommand


class test_class_base(unittest.TestCase):
    """class for testing class base model"""

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(console.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_pep8(self):
        style = pep8.StyleGuide()
        filenames = ["console.py"]
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0)
