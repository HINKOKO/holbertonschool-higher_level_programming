#!/usr/bin/python3
"""Module 12 - Pascal is on fire !"""


def pascal_triangle(n):
    """returns a list of lists
    of integers representing the
    Pascal's triangle of n"""
    if n <= 0:
        return [[]]
    elif n == 1:
        return [[1]]
    else:
        pascal = []
        for row in range(n):
            newrow = [1]
            for col in range(1, row + 1):
                newcell = newrow[col - 1] * float((row + 1 - col) / col)
                newrow.append(int(newcell))
            pascal.append(newrow)
        return pascal
