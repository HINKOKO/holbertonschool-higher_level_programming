#!/usr/bin/python3
"""Module 6 - Create Object from
a JSON file"""
import json


def load_from_json_file(filename):
    """same sentence as module description
    using json.load() method"""
    with open(filename) as f:
        py_object = json.load(f)
        return py_object
