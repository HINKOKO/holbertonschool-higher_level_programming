#!/usr/bin/python3
def print_last_digit(number):
    if 0 < number <= 9:
        ld = number
    elif number < 0:
        ld = ((number * -1) % 10)
    else:
        ld = number % 10
    print(ld, end='')
    return (ld)
