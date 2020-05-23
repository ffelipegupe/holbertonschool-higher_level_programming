#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the function max_integer
    """
    
    def test_okCase(self):
        """Function to test the ok'ed tests"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1, 0, 2]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-5, -6, -7, -3]), -3)
        self.assertEqual(max_integer([0, 1.2, 2.1, 5.6]), 5.6)
        self.assertEqual(max_integer("Zz"), "z")
        self.assertEqual(max_integer(["a", "b", "z"]), "z")

if __name__ == '__main__':
    unittest.main()
