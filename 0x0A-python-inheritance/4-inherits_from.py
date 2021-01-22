#!/usr/bin/python3
"""
inherits_from module
"""


def inherits_from(obj, a_class):
    """
    Function checks if an object is an instance of a class that
    inherits from a specific class, but not class itself
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
