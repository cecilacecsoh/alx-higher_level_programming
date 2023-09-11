#!/usr/bin/python3

"""
This is a module container of the function 2-is_same_class
"""

def is_same_class(obj, a_class):

    if type(obj) is not a_class:
        return False
    else:
        return True
