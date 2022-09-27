#!/usr/bin/python3
"""Module 7 - Integer validator"""


class BaseGeometry:
    """class continuing"""

    def area(self):
        """aera method to be continued"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """purpose : validating value
        which must be an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
