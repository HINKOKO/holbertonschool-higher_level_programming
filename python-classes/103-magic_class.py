#!/usr/bin/python3
"""
Magic Module for MagicClass
"""
import math


class MagicClass:
    """MagicClass
    Defines a class for computing perimeter
    """

    def __init__(self, radius):
        """check for radius valid data"""
        if type(radius) is not int and \
                type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            return self.__radius

    def area(self):
        return self.__radius * 2 * pi
