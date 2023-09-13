#!/usr/bin/python3
"""
A class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """A BaseGeometry class with public attribute area."""
    def area(self):
        """this raises an exception when called"""
        raise Exception("the area() is not implemented")
