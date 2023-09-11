#!/usr/bin/python3

"""
A container of MyList class inherit from list
"""


class MyList(list):
    """MyList class that inherited from list"""
    def __init__(self):
        """helps initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
