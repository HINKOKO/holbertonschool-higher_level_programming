#!/usr/bin/python3
from cmath import pi


class MagicClass:
    def __init__(self, radius):
        if type(radius) is not int and \
                type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            return self.radius

    def area(self):
        return self.radius * 2 * pi
