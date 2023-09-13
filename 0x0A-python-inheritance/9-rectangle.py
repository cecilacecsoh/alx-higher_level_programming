#!/usr/bin/python3

""" class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    (task based on 8-rectangle.py)"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Clas rpresentation of a rectangle"""

    def __init__(self, width, height):
        """
        the nitialization function
            Args:
                width: the width of a rectangle
                height: the length of a rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """this returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """an informal string representation of a rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
