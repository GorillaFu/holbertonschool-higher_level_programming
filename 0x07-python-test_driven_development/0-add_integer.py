#!/usr/bin/python3
"""
Function add two integers
Return: result of a+b
"""


def add_integer(a, b=98):
    """checks if a and b ints, returns result a+b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
