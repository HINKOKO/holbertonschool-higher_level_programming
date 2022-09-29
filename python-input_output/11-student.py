#!/usr/bin/python3
"""Module 11 - Student to disk and reload"""


class Student:
    """ Defines a student with public instance
    attributes:
                    - first_name
                    - last_name
                    - age
            Public Methods
                    - to_json
                    - reload_from_json"""

    def __init__(self, first_name, last_name, age):
        """Initialize student with
        first&last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns--if attrs is None-- a dictionary representation
        of a Student() instance
        Otherwise only the dict representation of attrs provided"""
        if attrs is not None:
            dict = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    dict[i] = self.__dict__[i]
            return dict
        else:
            # variante !
            return vars(self)

    def reload_from_json(self, json):
        print(json)
