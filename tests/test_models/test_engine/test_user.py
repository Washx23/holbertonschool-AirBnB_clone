""" Test for user class """
from models.user import User
import unittest

class Test_user(unittest.TestCase):

    def test_class(self):
        User_test = User()
        self.assertTrue(isinstance(User_test, User))
        self.assertIsInstance(User_test, User)
        self.assertTrue(hasattr(User_test, "email"))
        self.assertTrue(hasattr(User_test, "password"))
        self.assertTrue(hasattr(User_test, "first_name"))
        self.assertTrue(hasattr(User_test, "last_name"))
        self.assertEqual(User_test.email, "")
        self.assertEqual(User_test.password, "")
        self.assertEqual(User_test.first_name, "")
        self.assertEqual(User_test.last_name, "")

if __name__ == '__main__':
    unittest.main()
