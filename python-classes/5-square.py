#!/usr/bin/python3
"""
Module - 4
Defines a class Square with private size
Checks for size type and value and valid it
"""


class Square:
    """
    class Square
    Instantiation with size
    """

    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            private one, __size, must be of type int
            or greater than 0
            """
        self.__size = size

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes area of square an returns it
        """
        return (self.__size) ** 2

    def my_print(self):
        """
        Prints the square on screen
        of size size
        """
        print("\n".join("#" * self.__size for rows in range(self.__size)))
