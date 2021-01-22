#!/usr/bin/python3
""" squre class module"""
Rectangle = __import__('9-rectangle').Rectangle


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
