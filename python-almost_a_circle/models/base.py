#!/usr/bin/python3
""" 1 - Base class"""

import os


class Base:
    """Base class
    with private class attribute
    Instantiation with __init__ """
    __nb_objects = 0

    def __init__(self, id=None):
        """id set to id if not None"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
