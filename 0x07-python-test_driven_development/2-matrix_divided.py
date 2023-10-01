#!/usr/bin/python3

"""
    task 2-matrix_divided Module
"""


def matrix_divided(matrix, div):
    """
        Divides all the elements of a matrix

        Args:
            matrix: intial 2D list
            div: an int which is the divisor

        Returns:
            New matrix thats containing the divided elements
            rounded to two decimal places
    """
    prevs_len = 0
    error_messg = "the matrix must be a matrix(list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_messg)

    for block in matrix:    # matrix is a list
        if type(block) is not list:
            raise TypeError(error_messg)

        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error_messg)

        if len(block) != prevs_len and prevs_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        prevs_len = len(block)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
