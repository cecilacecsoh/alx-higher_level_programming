#!/usr/bin/python3
"""
function that returns True if the object is exactly an
instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Checking if the object is exactly an instance of the specified class
        Args:
            obj: an initial object
            a_class: a class to confirm with the object
            Returns: True if object is an exactly the instance,
                     else False if not
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
