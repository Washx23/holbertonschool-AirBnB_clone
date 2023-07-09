""" Test for review class """
from models.review import Review
import unittest

class Test_review(unittest.TestCase):

    def test_class(self):
        Review_test = Review()
        self.assertTrue(isinstance(Review_test, Review))
        self.assertIsInstance(Review_test, Review)
        self.assertTrue(hasattr(Review_test, "place_id"))
        self.assertTrue(hasattr(Review_test, "user_id"))
        self.assertTrue(hasattr(Review_test, "text"))
        self.assertEqual(Review_test.place_id, "")
        self.assertEqual(Review_test.user_id, "")
        self.assertEqual(Review_test.text, "")

if __name__ == '__main__':
    unittest.main()
