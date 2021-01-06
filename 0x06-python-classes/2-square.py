#!/usr/bin/python3
class Square:
    """square class"""
    def __init__(self, size=0):
        """size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
