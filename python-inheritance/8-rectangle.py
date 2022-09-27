#!/usr/bin/python3
""" Module 8 - Rectangle
We import parent class ``BaseGeometry
since Rectangle class inherits from it"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry
    Methods: instantiation with __init__"""

    def __init__(self, width, height):
        """initialize width and height after
        validating them with integer_validator"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
