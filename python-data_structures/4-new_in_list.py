#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list[0:]
    if idx >= 0 and idx < len(my_list):
        new[idx] = element
        return new
    return my_list
