#!/usr/bin/python3
""""
is_same_class module
"""


def is_same_class(obj, a_class):
    """
    Function that checks if object is instance of
    a given class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
