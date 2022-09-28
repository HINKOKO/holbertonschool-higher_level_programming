#!/usr/bin/python3
"""Module 10 - Square #1
Inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle which
        inherited from BaseGeometry
        Methods: init and area"""

    def __init__(self, size):
        """Instantiation with size
wich must be private and positive integer
Check accomplished by integer_validator"""
        self.integer_validator("size", size)
        super().__init__(size, size)
