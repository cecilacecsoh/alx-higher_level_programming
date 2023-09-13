#!/usr/bin/python3

"""
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representation of a rectangle and
       Class that inherits from the BaseGeometry.
    """
    def __init__(self, width, height):
        """Initializing the  function
            Args:
                width: width variable to be initialized
                height: height variable to be initialized
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("the height", height)
        self.__height = height
