#!/usr/bin/python3
import io
import unittest
import sys
from models.base import Base
from models.square import Square
"""
Unittests for Square class
"""


class Test_Square(unittest.TestCase):
    """ test """

    def test_Square1(self):
        """
        chk  id
        """
        S1 = Square(5)
        self.assertEqual(S1.id, 11)
        S2 = Square(5, 2, 1, 48)
        self.assertEqual(S2.id, 48)

    def test_Square2(self):
        """
        Validate id
        """
        S3 = Square(10, 2, 0, "hi")
        self.assertEqual(S3.id, "hi")
        S4 = Square(10, 2, 0, [12, 10])
        self.assertEqual(S4.id, [12, 10])
        S5 = Square(10, 2, 0, {"key": 12, "value": 20})
        self.assertEqual(S5.id, {'key': 12, 'value': 20})
        S6 = Square(10, 2, 0, (12, 10))
        self.assertEqual(S6.id, (12, 10))

if __name__ == "__main__":
    unittest.main()
