#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for i in str:
        if n >= 0:
            newstr = str[:n] + str[n + 1:]
            return newstr
        else:
            return str
