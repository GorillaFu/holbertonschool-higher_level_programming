#!/usr/bin/python3
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""
Unittests for Rectangl
"""


class Test_Rectangle(unittest.TestCase):
    """  test fo Rectangle """

    def test_Rectangle1(self):
        """
        check id
        """
        R1 = Rectangle(10, 2)
        self.assertEqual(R1.id, 4)
        R2 = Rectangle(2, 10)
        self.assertEqual(R2.id, 5)
        R3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(R3.id, 12)

if __name__ == "__main__":
    unittest.main()
