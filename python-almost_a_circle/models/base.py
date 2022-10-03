#!/usr/bin/python3
""" 1 - Base class"""


class Base:
	"""Base class
	with private class attribute
	Instantiation with __init__ """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = id
