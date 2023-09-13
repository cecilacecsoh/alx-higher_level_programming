#!/usr/bin/python3
"""
A class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """A BaseGeometry class with public instance methods
        area and integer_validator"""
    def area(self):
        """ that raises an exception when called"""
        raise Exception("An area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is a integer > 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be >  0".format(name))
