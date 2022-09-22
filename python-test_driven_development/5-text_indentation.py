#!/usr/bin/python3
"""Module 5 - Text Indentation"""


def text_indentation(text):
    """ 'text' must be a string
        returns a revised text
        where each ?:. has been replaced with 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        flag = False
        for char in text:
            if flag:
                if char == " ":
                    continue
                flag = False
            if char == '.' or char == '?' or char == ':':
                print(char)
                print("")
                flag = True
            else:
                print(char, end="")
