#!/usr/bin/python3
"""Module 12 - Pascal is on fire !"""


def pascal_triangle(n):
    """returns a list of lists
    of integers representing the
    Pascal's triangle of n"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        result = []
        for row in range(n):
            newrow = [1]
            for cols in range(1, row + 1):
                newcell = newrow[cols - 1] * (row + 1 - cols)/cols
                newrow.append(int(newcell))
            result.append(newrow)
        return result
