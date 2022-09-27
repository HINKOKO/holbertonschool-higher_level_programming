#!/usr/bin/python3
"""Module 2 -  Exact same object"""


def is_same_class(obj, a_class):
    """Returns True if the obj is exactly
    only exactly an instance of a_class
    False otherwise"""
    if type(obj) == a_class:
        return True
    return False
