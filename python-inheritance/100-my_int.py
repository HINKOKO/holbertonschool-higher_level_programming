#!/usr/bin/python3
"""Module 100 - My Rebel Integer"""


class MyInt(int):
    """Inverts == and !="""

    def __init__(self, val1):
        self.val1 = val1

    def __equality__(self, val2):
        """Returns True if not equal"""
        return self.val1 != val2

    def __invert__(self, val2):
        """Returns True if equals"""
        return self.val1 == val2
