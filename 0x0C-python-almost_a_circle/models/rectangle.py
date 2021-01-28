#!/usr/bin/python3
""" REctangle class """
from models.base import Base


class Rectangle(Base):
    """
    rectangle subclass of base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """validate value and set height to value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """validate value and set height to value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """validate value and set height to value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """"Draws the rectangle + x y translation"""
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + '\n') * self.height, end="")

    def __str__(self):
        """
        Print string representation of attributes
        """
        fmat = "[Rectangle] ({}) {}/{} - {}/{}"
        s = fmat.format(self.id, self.x, self.y, self.width, self.height)
        return s

    def update(self, *args, **kwargs):
        """Updates rectangle"""
        if not args and not kwargs:
            return
        if args:
            param = ["id", "width", "height", "x", "y"]
            for i, atr in enumerate(args):
                if i < len(param):
                    setattr(self, param[i], atr)
        else:
            for j, val in kwargs.items():
                if hasattr(self, j):
                    setattr(self, j, val)

    def to_dictionary(self):
        """dictionary"""
        result = {}

        for i, val in self.__dict__.items():
            if i.startswith("_"):
                result[i.split("__")[-1]] = val
            else:
                result[i] = val
        return result
