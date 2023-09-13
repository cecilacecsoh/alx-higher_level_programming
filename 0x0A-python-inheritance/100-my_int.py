#!/usr/bin/python3

"""
A class MyInt that inherits from int
"""


class MyInt(int):
    """A class MyInt that inherits from class int"""

    def __eq__(self, other):
        """ this overrides equals, inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """ it overrides not-equals, inverting it"""
        return int(self) == int(other)
