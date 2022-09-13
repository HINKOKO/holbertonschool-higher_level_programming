#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        sqd_matrix = [[elm*elm for elm in inner] for inner in matrix]
        return sqd_matrix
    return matrix
