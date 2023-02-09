#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for row in matrix:
        res_row = []
        for item in row:
            res_row.append(item**2)
        res.append(res_row)
    return res