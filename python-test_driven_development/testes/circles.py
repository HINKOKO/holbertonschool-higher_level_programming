#!/usr/bin/python3
"""Module circle area"""
from matrixh import pi


def circle_area(r):
    """returns circle area"""
    if type(r) not in [int, float]:
        raise TypeError("Radius must be non-negative REAL number monkey")
    if r < 0:
        raise ValueError("radius can't be negative")
    return pi*(r**2)
