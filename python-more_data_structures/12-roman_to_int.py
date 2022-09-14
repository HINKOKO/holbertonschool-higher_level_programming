#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        r = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        res = 0
        for i in range(len(roman_string)):
            if i > 0 and r[roman_string[i]] > r[roman_string[i - 1]]:
                res += r[roman_string[i]] - 2 * r[roman_string[i - 1]]
            else:
                res += r[roman_string[i]]
        return res
    else:
        return 0
