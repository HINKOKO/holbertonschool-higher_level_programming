#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_l = my_list[0:]
    if idx >= 0 and idx < len(my_list) - 1:
        new_l[idx] = element
        return (new_l)
    return (my_list)
