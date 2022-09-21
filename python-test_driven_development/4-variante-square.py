#!/usr/bin/python3
"""Doc on module"""


def print_square(size):
    """Doc on function"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(0, size):
        for cols in range(0, size):
            if cols != (size - 1):
                print("#", end="")
            else:
                print("#")
