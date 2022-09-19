#!/usr/bin/python3
"""
Module 1
Defines class square with private instance attribute 'size'
"""


class Square:
    """
    class Square
    """

    def __init__(self, size):
        """
        attribute size is make private
        with double underscore as prefix
        Instantiation with size
        """
        self.__size = size
