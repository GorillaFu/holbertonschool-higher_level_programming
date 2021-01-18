#!/usr/bin/python3
"""
Function that divide a matrix
Return the value of each element of the matrix
"""


def matrix_divided(matrix, div):
    """Function that divide matrix"""
    result = []

    rowback = len(matrix[0])

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        result.append([])
        if(len(matrix[i]) is not rowback):
            raise TypeError("Each row of the matrix matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of list) of integers/floats")
            result[i].append(round(matrix[i][j] / div, 2))
            rowback = len(matrix[i])
    return result
