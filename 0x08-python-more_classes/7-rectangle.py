#!/usr/bin/python3
""" Write an empty class Rectangle that defines a rectangle """


class Rectangle:
    """ Rectanhle class with pvt height+width attributes """
    number_of_instances = 0
    print_sumbol = "#"

    def __init__(self, width=0, height=0):
        """ constructor func """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns area of rectanhle"""
        return self.width * self.height

    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ returns str image of rectangle """
        if self.height == 0 or self.width == 0:
            return ""
        rect = ""
        for i in range(self.height):
            for j in range(self.width):
                rect += str(self.print_symbol)
            rect += "\n"
        rect = rect[:-1]
        return rect

    def __repr__(self):
        """return function representation of rectangle object """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """if rect delete print msg"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
