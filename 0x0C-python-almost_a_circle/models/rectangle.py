#!/usr/bin/python3
""" REctangle class """
from models.base import Base


class Rectangle(Base):
    """
    rectangle subclass of base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """validate value and width to value"""
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value <= 0:
            raise TypeError("value must be greater than 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """validate value and set height to value"""
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value <= 0:
            raise TypeError("value must be greater than 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """validate value and set height to value"""
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value <= 0:
            raise TypeError("value must be greater than 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """validate value and set height to value"""
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value <= 0:
            raise TypeError("value must be greater than 0")
        self.__y = value
