""" Test for place class """


from models.place import Place
import unittest


class Test_place(unittest.TestCase):

    def test_class(self):
        Place_test = Place()
        self.assertTrue(isinstance(Place_test, Place))
        self.assertIsInstance(Place_test, Place)
        self.assertTrue(hasattr(Place_test, "city_id"))
        self.assertTrue(hasattr(Place_test, "user_id"))
        self.assertTrue(hasattr(Place_test, "name"))
        self.assertTrue(hasattr(Place_test, "description"))
        self.assertTrue(hasattr(Place_test, "number_rooms"))
        self.assertTrue(hasattr(Place_test, "number_bathrooms"))
        self.assertTrue(hasattr(Place_test, "max_guest"))
        self.assertTrue(hasattr(Place_test, "price_by_night"))
        self.assertTrue(hasattr(Place_test, "latitude"))
        self.assertTrue(hasattr(Place_test, "longitude"))
        self.assertTrue(hasattr(Place_test, "amenity_ids"))
        self.assertEqual(Place_test.city_id, "")
        self.assertEqual(Place_test.user_id, "")
        self.assertEqual(Place_test.name, "")
        self.assertEqual(Place_test.description, "")
        self.assertEqual(Place_test.number_rooms, 0)
        self.assertEqual(Place_test.number_bathrooms, 0)
        self.assertEqual(Place_test.max_guest, 0)
        self.assertEqual(Place_test.price_by_night, 0)
        self.assertEqual(Place_test.latitude, 0.0)
        self.assertEqual(Place_test.longitude, 0.0)


if __name__ == '__main__':
    unittest.main()
