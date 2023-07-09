""" Test for state class """


from models.state import State
import unittest


class Test_state(unittest.TestCase):

    def test_class(self):
        State_test = State()
        self.assertTrue(isinstance(State_test, State))
        self.assertIsInstance(State_test, State)
        self.assertTrue(hasattr(State_test, "name"))
        self.assertEqual(State_test.name, "")


if __name__ == '__main__':
    unittest.main()
