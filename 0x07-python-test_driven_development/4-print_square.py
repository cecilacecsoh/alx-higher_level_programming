#!/usr/bin/python3

"""
    4-print_square Module task
"""


def print_square(size):
    """
        It Prints a square with the character '#'

        Args:
            size: the size length of the square
    """
    if type(size) is not int:
        raise TypeError(" the size must be an integer")

    if size < 0:
        raise ValueError("the size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
