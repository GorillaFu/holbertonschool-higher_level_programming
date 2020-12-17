#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        cells = []
        for j in i:
            cells.append(j**2)
        new.append(cells)
    return new
