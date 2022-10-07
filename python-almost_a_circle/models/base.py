#!/usr/bin/python3
""" 1 - Base class"""
import json
import csv
from os.path import exists


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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        fname = cls.__name__ + ".json"
        lst = []
        if exists(fname):
            with open(fname, 'r') as f:
                inst = cls.from_json_string(f.read())
            for i in range(len(inst)):
                lst.append(cls.create(**inst[i]))
        return lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to comma-sep-values format"""
        csv_name = cls.__name__ + ".csv"
        with open(csv_name, 'w', newline='') as c:
            if list_objs is not None:
                list_objs = [a.to_dictionary() for a in list_objs]
                if cls.__name__ == "Square":
                    field_names = ['id', 'size', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    field_names = ['id', 'width', 'height', 'x', 'y']
                # thanks to https://docs.python.org/3/library/csv.html
                # thanks to https://www.programcreek.com/\
                # python/example/3190/csv.DictWriter
                writer = csv.DictWriter(c, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        # https://www.analyticsvidhya.com/blog/2021/08/\
        # python-tutorial-working-with-csv-file-for-data-science/#h2_2
        """deserializes from CSV, returns list of instances
        (just as load_from_file(cls) about JSON"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'widht', 'height', 'x', 'y']
                else:
                    fields = ['id', 'size', 'x', 'y']
                objs = csv.DictReader(csvfile, fieldnames=fields)
                objs = [dict([k, int(v)] for k, v in d.items())
                        for d in objs]
                return [cls.create(**d) for d in objs]
        except FileNotFoundError:
            return []
