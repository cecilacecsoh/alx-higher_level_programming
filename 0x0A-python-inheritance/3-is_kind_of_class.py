#!/usr/bin/python3
"""
a function that returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class ;
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Checking if the object is an instance of a specified class
        Args:
            obj: an initial object
            a_class: a class to confirm the object
            Returns: True if object is an instance of or inherited the class
                     otherwise False.
    """
    return isinstance(obj, a_class)
