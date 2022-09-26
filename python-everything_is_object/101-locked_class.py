#!/usr/bin/python3
"""Module 101 - Low memory cost"""


class LockedClass:
    """ The basic usage of __slots__ 
    is to save space in objects"""
    __slots__ = ['first_name']
