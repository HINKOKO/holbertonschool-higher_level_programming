#!/usr/bin/python3

from calculator_1 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        return c
    for i in range(4, 6):
        c = add(c, i)
    else:
        return sub(a, b)
