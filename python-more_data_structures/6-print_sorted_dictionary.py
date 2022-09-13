#!/usr/bin/python3
from typing import OrderedDict


def print_sorted_dictionary(a_dictionary):
    sdict = OrderedDict(sorted(a_dictionary.items()))
    return sdict
