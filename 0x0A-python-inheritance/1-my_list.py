#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """MyList class which inherits from list"""
    def __init__(self):
        """initializing the object"""
        super().__init__()
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
