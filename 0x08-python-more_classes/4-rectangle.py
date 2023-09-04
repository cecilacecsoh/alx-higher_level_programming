#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
"""

class Rectangle:
    """ A class rectangle"""
    def __init__(self, width=0, height=0):
        """ An Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width  """
        return self.__width

    @property
    def height(self):
        """ The height """
        return self.__height

    @width.setter
    def width(self, value):
        """A width setter """
        if type(value) is not int:
            raise TypeError("the width must be an integer")
        if value < 0:
            raise ValueError("the width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """A height setter """
        if type(value) is not int:
            raise TypeError("the height must be an integer")
        if value < 0:
            raise ValueError("the height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimiterof a rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ return the rectangle with the character # """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """ this return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)
