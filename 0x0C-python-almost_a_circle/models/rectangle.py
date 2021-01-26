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
