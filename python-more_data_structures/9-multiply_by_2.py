#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for elm in a_dictionary:
        new_dict[elm] = a_dictionary[elm] * 2
    return (new_dict)
