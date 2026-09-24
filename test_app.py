import unittest
from app import square, is_even

class TestApp(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_is_even(self):
        self.assertTrue(is_even(4))
