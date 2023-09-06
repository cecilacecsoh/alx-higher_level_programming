#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
"""


class Rectangle:
    """a class representation of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializing the rectangle by
        setting the objet with width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for  instance attribute width"""
        if type(value) is not int:
            raise TypeError("the width must be an integer")
        if value < 0:
            raise ValueError("the width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for  instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for attribute height"""
        if type(value) is not int:
            raise TypeError("the height must be an integer")
        if value < 0:
            raise ValueError("the height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns astring representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
