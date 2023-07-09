#!/usr/bin/python3
""" Test for amenity class """


from models.amenity import Amenity
import unittest


class Test_amenity(unittest.TestCase):

    def test_class(self):
        Amenity_test = Amenity()
        self.assertTrue(isinstance(Amenity_test, Amenity))
        self.assertIsInstance(Amenity_test, Amenity)
        self.assertTrue(hasattr(Amenity_test, "name"))
        self.assertEqual(Amenity_test.name, "")


if __name__ == '__main__':
    unittest.main()
