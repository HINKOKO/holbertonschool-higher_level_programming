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
        return self.width

    @size.setter
    def size(self, value):
        """Setter, protect the size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """overloading str pattern for square"""
        sq = ("[Square] ({}) {}/{} - {}".format(self.id,
                                                self.x, self.y, self.size))
        return sq

    def update(self, *args, **kwargs):
        """assign attributes to list *args
        or to dict **kwargs"""
        if len(args) != 0 and args is not None:
            for j, k in enumerate(args):
                if j == 0:
                    self.id = k
                elif j == 1:
                    self.size == k
                elif j == 2:
                    self.x = k
                elif j == 3:
                    self.y = k
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
