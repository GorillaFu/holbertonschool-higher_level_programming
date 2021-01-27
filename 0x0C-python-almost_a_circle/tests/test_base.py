#!/usr/bin/python3
"""unit tests for base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """base tests"""
    def test_validate(self):
        """ validate id number"""
        t1 = Base()
        self.assertEqual(t1.id, 1)
        t2 = Base()
        self.assertEqual(t2.id, 2)
        t3 = Base()
        self.assertEqual(t3.id, 3)

    def test_validate1(self):
        """ validate id number with parameters"""
        t4 = Base(25)
        self.assertEqual(t4.id, 25)
        t5 = Base(-13)
        self.assertEqual(t5.id, -13)

    def test_validate2(self):
        """ validate the id number with extra args"""
        with self.assertRaises(TypeError):
            t6 = Base(3, 7)

    def test_validate3(self):
        """ validate if the args is string """
        t7 = Base("13")
        self.assertEqual(t7.id, "13")

if __name__ == "__main__":
    unittest.main()
