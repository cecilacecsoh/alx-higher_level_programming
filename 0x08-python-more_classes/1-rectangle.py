#!/usr/bin/python3
""" an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The width """
        return self.__width

    @property
    def height(self):
        """ The height """
        return self.__height

    @width.setter
    def width(self, value):
        """ A width setter """
        if type(value) is not int:
            raise TypeError(" A width must be an integer")
        if value < 0:
            raise ValueError(" A width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ A height setter """
        if type(value) is not int:
            raise TypeError(" a height must be an integer")
        if value < 0:
            raise ValueError("a height must be >= 0")
        self.__height = value
