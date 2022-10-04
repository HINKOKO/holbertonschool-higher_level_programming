#!/usr/bin/python3
"""class Square
Inherits from Rectangle"""
from sys import argv
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle
    Call to super class
    All attributes from Rectanlge are used"""

    def __init__(self, size, x=0, y=0, id=None):
        """super call and width and height turned into
        size, since square is the special rectangle
        where width == height == size"""
        super().__init__(size, size, x, y, id)
        self.size = size

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
        or to dict **kwargs
                if args: set in this order, (important!), id,size
                x, y
                if no args, set attributes according to kwargs"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
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
