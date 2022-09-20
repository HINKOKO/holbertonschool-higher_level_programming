#!/usr/bin/python3
"""
Module - 4
Defines a class Square with private size
Checks for size type and value and valid it
Ability to retrieve and update size and position
with getter and setter, @property and @**.setter respectively
"""


class Square:
    """
    class Square
    Instantiation with size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square
        Attributes:
            size: must be of type int
            or greater than 0
            position: tuple of two positive int
            """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter, sets the size to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter, retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position to a value"""
        if type(value) is not tuple or len(value) != 2 or type(value[0]) \
                is not int or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Computes area of square an returns it"""
        return (self.__size) ** 2

    def my_print(self):
        """Prints the square on screen with #char
        of size '
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end='')
            print("\n".join(" " * self.__position[0] +
                            "#" * self.__size for rows in range(self.__size)))
