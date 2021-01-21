#!/usr/bin/python3
"""
    Pascal triangle
"""


def pascal_triangle(n):
    """Pascal Triangle"""
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]
        if triangle:
            for j in range(i):
                row.append(sum(triangle[-1][j:j+2]))
        triangle.append(row)

    return triangle
