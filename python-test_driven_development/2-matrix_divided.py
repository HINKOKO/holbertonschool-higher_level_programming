#!/usr/bin/python3
"""Module 2 - matrix divided !
Divides all elements of a matrix
matrix must be a list of integers or floats
"""


def matrix_divided(matrix, div):
    """matrix division
    -matrix must be a list of integers or floats
    -Each row of the matrix must be of the same size
    -div must be a a number and a positive one dude"""
    error_int_float = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(error_int_float)

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    elif not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    else:
        len_check = len(matrix[0])
        new_matrix = []
        for row in matrix:
            if type(row) is not list:
                raise TypeError(error_int_float)

            if len(row) != len_check:
                raise TypeError(
                    "Each row of the matrix must have the same size")
            new_cols = []
            for i in row:
                if not isinstance(i, (int, float)):
                    raise TypeError(error_int_float)
                new_cols.append(round(i/div, 2))
            new_matrix.append(new_cols)
        return new_matrix
