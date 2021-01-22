#!/usr/bin/python3
"""
empty geometry class module
"""


class BaseGeometry:
    """
    class BaseGeometry.
    """
    def area(self):
        """
        method that raises error exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method for validating if value is int
        """
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")
