#!/usr/bin/python3
"""*
Module - 3
Prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """say_my_name
    -Print the first and last name
    -Both must be strings"""
    if type(first_name) is not str:
        raise TypeError("{:s} must be a string".format("first_name"))
    if type(last_name) is not str:
        raise TypeError("{:s} must be a string".format("last_name"))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
