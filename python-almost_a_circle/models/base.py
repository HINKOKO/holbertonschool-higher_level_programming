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
        record = []
        if list_objs is not None:
            for inst in list_objs:
                record.append(cls.to_dictionary(inst))
            fname = cls.__name__ + ".json"
            with open(fname, "w") as f:
                f.write(cls.to_json_string(record))

    @staticmethod
    def from_json_string(json_string):
        """static method-returns the list of JSON string
        representation ``json_strings``"""
        json_list = "[]"
        if json_string is not None or len(json_string) != 0:
            return json.loads(json_string)

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

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        record_name = cls.__name__ + ".json"
        book = []
        if os.path.exists(record_name):
            with open(record_name, "r") as record:
            book.append(cls.create())
        return book
