#!/usr/bin/python3
"""
is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    checks if object is an instance of class or
    a class that inherits from og class
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
