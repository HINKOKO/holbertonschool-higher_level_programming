#!/usr/bin/python3
"""Module 13 - Can I ?
Adds new attribute if possible, can I ?"""


def add_attribute(obj, name, value):
    """set attribute of name 'name'
    with 'value' value if not present in dict"""
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
