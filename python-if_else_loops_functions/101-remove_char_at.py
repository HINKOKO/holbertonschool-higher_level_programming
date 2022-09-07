#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for i in str:
        newstr = str[0: n] + str[n + 1::]
    return newstr
