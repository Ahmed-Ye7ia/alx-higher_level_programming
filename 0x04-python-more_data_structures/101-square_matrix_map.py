#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(map(lambda x: x*x, matrix), matrix))
