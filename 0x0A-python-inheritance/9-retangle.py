#!/usr/bin/python3
"""
rectangle subclass of basegeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectanngle class that inherits attributes from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        """
        return string representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        return rect area
        """
        return self.__width * self.__height
