""" Test for city class """
from models.city import City
import unittest

class Test_city(unittest.TestCase):

    def test_class(self):
        City_test = City()
        self.assertTrue(isinstance(City_test, City))
        self.assertIsInstance(City_test, City)
        self.assertTrue(hasattr(City_test, "state_id"))
        self.assertTrue(hasattr(City_test, "name"))
        self.assertEqual(City_test.state_id, "")
        self.assertEqual(City_test.name, "")

if __name__ == '__main__':
    unittest.main()
