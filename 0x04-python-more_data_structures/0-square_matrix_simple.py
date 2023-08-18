#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squaredmtx = []
    for line in matrix:
        squaredmtx.append([c**2 for c in line])

    return (squaredmtx)
