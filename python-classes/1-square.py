#!/usr/bin/python3
"""
Module 1
Defines class square with private instance attribute 'size'
"""


class Square:
    """class Square.
        Instantiation with size
        Note that size is here a private instance attribute
    """

    def __init__(self, size):
        """
        Initializes the data for class square.
        """
        self.__size = size
