#!/usr/bin/python3

"""
    101-lazy_matrix_mul Module/task
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        Multiplies 2 matrices

        Args:
            m_a: 1st matrix(2D List)
            m_b: 2nd matrix(2D List)

        Returns:
            The product of input two matrices
    """
    return np.matmul(m_a, m_b)
