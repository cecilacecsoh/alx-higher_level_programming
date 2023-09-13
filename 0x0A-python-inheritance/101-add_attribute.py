#!/usr/bin/python3

"""
A function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, objname, value):
    """ adds a new attribute to an object if it’s possible
    args:
        obj: a class object
        objname: an object name
        value: the value of attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("This can not add new attribute")
    setattr(obj, objname, value)
