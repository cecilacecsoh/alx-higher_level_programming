#!/usr/bin/python3
"""
A container of MyList class inherit from list
"""


class MyList(list):
    """MyList class that's inherited from list"""
    def __init__(self):
        """ initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
