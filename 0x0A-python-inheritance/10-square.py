#!/usr/bin/python3
"""
square + rectangle subclass of basegeometry class
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

class Square(Rectangle):
    """
    square class based on rectangle class
    """

    def __init__(self, size):
        """
        constructor
        """
        self.__size = size

    def area(self):
        """
        return area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        return str representation
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
