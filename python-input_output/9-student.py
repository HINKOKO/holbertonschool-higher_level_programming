#!/usr/bin/python3
"""Module 9 - Student to JSON"""


class Student:
    """ Defines a student with public instance
    attributes:
            -first_name
            -last_name
            -age"""

    def __init__(self, first_name, last_name, age):
        """Instantiation and public method:
        - to_json > retrieves a dictionary
         representation of a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
