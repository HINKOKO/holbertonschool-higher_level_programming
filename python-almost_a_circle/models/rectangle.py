#!/usr/bin/python3
"""Module 2. First Rectangle
Creates a Rectangle class, which inherits
from class Base (base.py)"""
from models.base import Base


class Rectangle(Base):
    """Private instance attributes width, height, x, y
        Setter allows us to 'protect' width, height,\
        x and y from bad data, and Getter (@property) allows us\
        to retrieve the values we need
    Public methods:
        - area()
        - display()*
        -__str__ (overriden)
        """

    def __init__(self, width, height, x=0,
                 y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter, gettin' width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter - setting the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """gettin' x """
        return self.__x

    @property
    def y(self):
        """gettin' y"""
        return self.__y

    @x.setter
    def x(self, value):
        """Setting x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Setting y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area value of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints on stdout the Rectangle instance
        with character #"""
        for a in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for b in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Overrides the __str__ method"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))
