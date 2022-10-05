#!/usr/bin/python3
""" 1 - Base class"""
import json
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string rep of
        list_dictionaries"""
        if list_dictionaries is None:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method - writes the JSON string rep
        of list_obj to a file"""
        fname = cls.__name__ + ".json"
        record = []
        if list_objs is not None:
            for i in list_objs:
                record.append(cls.to_dictionary(i))
        with open(fname, "w+") as f:
            f.write(cls.to_json_string(record))

    @staticmethod
    def from_json_string(json_string):
        """static method-returns the list of JSON string
        representation ``json_strings``"""
        json_list = []
        if json_string is not None:
            return json.loads(json_string)
        return json_list

    @classmethod
    def create(cls, **dictionary):
        """class method- returns an instance with all
        attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
