#!/usr/bin/python3
"""Module 5-text_indentation"""


def text_indentation(text):
    """Text_indentation
    - Text must be a string
    - Replace each . ? : with 2 newlines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        replacer = {'?': '?\n\n', '.': '.\n\n', ':': ':\n\n'}
        for key, value in replacer.items():
            text = text.replace(key, value)
        text = text.replace('\n ', '\n')
        print(text)
