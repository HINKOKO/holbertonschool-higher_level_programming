#!/usr/bin/python3
def weight_average(my_list=[]):
    average = sum([i[0]*i[1] for i in my_list]) / \
        (sum([i[1] for i in my_list]))
    return average
