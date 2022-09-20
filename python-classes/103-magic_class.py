#!/usr/bin/python3
"""
Magic Module for MagicClass
"""
import math


class MagicClass:
    """MagicClass
    Defines a class for computing perimeter and aera
        of a circle with parameter radius
    """

    def __init__(self, radius=0):
        """check for radius valid data type"""
        self.__radius = 0
        if type(radius) is not int and \
                type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Computes area according to radius"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Computes circumference according to radius"""
        return 2 * self.__radius * math.pi
