#!/usr/bin/python3

""" 0-add_integer Module """


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: 1st integer
        b: 2nd integer

    Returns:
        addition of two the integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a mmust be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        new_a, new_b = int(a), int(b)
        return new_a + new_b
