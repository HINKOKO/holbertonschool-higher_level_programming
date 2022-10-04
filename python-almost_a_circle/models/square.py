#!/usr/bin/python3
"""class Square
Inherits from Rectangle"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle
    Call to super class
    All attributes from Rectanlge are used"""

    def __init__(self, size, x=0, y=0, id=None):
        """super call and width and height turned into
        size, since square is the special rectangle
        where width == height == size"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter, used to retrieve size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter, protect the size attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def __str__(self):
        """overloading str pattern for square"""
        sq = ("[Square] ({}) {}/{} - {}".format(self.id,
                                                self.x, self.y, self.__width))
        return sq
