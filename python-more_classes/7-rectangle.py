#!/usr/bin/python3
"""Module 7 - Change representation"""


class Rectangle:
    """ Defines a rectangle
    - Private attribute width and height """

    number_of_instances = 0
    print_symbol = ("#")

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area"""
        return ((self.width) * (self.height))

    def perimeter(self):
        """Computes perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width)*2

    def __str__(self):
        """Prints the rectangle with pattern #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ("\n".join(str(self.print_symbol) * self.width for x in range(self.height)))

    def __repr__(self):
        """Prints the rectangle with pattern #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """display message when instance deletion occurs"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
