#!/usr/bin/python3
from typing import OrderedDict


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
