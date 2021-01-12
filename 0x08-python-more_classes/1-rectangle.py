#!/usr/bin/python3
""" Write an empty class Rectangle that defines a rectangle """


class Rectangle:
    """ Rectanhle class with pvt height+width attributes """
    def __init__(self, width=0, height=0):
        """ constructor func """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method Width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method with validation """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method height w validation """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
