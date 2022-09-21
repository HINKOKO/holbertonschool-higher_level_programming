#!/usr/bin/python3
"""Module 0 - Integers addition
Contains one method(function)
Method takes 2 values as parameters
CAsts ,them into integers and adds them"""


def add_integer(a, b=98):
    """
    returns a + b
    After having checked a and b are integer or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
