#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list[:]
    if my_list:
        for x in my_list:
            new.append(False if x % 2 else True)
    return new
