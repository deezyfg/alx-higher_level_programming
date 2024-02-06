#!/usr/bin/python3
"""Module defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle of size n.

    Args:
        n: The size of the desired Pascal's Triangle.
           Should be a positive integer.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
