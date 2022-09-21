#!/usr/bin/python3
"""
Module - 4
Prints a square of size size!
"""


def print_square(size):
    """print_square
    -size is the lenght of the square
    -size must be an integer and greater than 0"""
    integer = "size must be an integer"
    if type(size) is not int:
        raise TypeError(integer)
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError(integer)
    else:
        print("\n".join("#"*size for rows in range(size)))
