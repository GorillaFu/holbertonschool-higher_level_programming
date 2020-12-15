#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        print()
    else:
        for row in matrix:
            i = 1
            for val in row:
                if i < len(row):
                    print("{:d} ".format(val), end = "")
                else:
                    print("{:d}".format(val))
            i+=1
