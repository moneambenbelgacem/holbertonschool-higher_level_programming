#!/usr/bin/python3
"""Module have one function"""


def matrix_divided(matrix, div):
    """divide matrix"""
    a = "matrix must be a matrix (list of lists) of integers/floats"
    row_len = len(matrix[0])
    if not isinstance(matrix, list):
        raise TypeError("{:s}".format(a))
    for row in matrix[1:]:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
