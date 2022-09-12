#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        max_value = my_list[0]
        for num in my_list:
            if num > max_value:
                num = max_value
        return (num)
    else:
        return None
