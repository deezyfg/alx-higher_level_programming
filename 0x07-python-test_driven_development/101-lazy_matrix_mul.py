#!/usr/bin/python3.5
"""
Module defining a function for matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies two matrices using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        The result of the matrix multiplication.
    """

    return (np.matmul(m_a, m_b))
