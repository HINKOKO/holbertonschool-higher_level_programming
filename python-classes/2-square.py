#!/usr/bin/python3
"""
Module - 2
Defines a class Square with private size
Checks for size type and value and valid it
"""


class Square:
    """
    class Square
    Instantiation with size
    """

    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            private one, __size, must be of type int
            or greater than 0
            """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
