#!/usr/bin/python3
"""Square class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        fmat = "[Square] ({}) {}/{} - {}"
        s = fmat.format(self.id, self.x, self.y, self.width)
        return s

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size set"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates rectangle"""
        if not args and not kwargs:
            return
        if args:
            param = ["id", "size", "x", "y"]
            for i, atr in enumerate(args):
                if i < len(param):
                    setattr(self, param[i], atr)
        else:
            for j, val in kwargs.items():
                if hasattr(self, j):
                    setattr(self, j, val)

    def to_dictionary(self):
        """square to dictionary"""
        dic = super().to_dictionary()
        dic["size"] = dic["width"]
        del dic["width"]
        del dic["height"]
        return dic
