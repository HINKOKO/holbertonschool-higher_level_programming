#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    res = 0
    for i in range(len(roman_string) - 1):
        left = roman_string[i]
        right = roman_string[i + 1]
        if r[left] < r[right]:
            res -= r[left]
        else:
            res += r[left]
    res += r[roman_string[-1]]
    return res
