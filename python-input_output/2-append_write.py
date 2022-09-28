#!/usr/bin/python3
"""Module 2 - Append to a file"""


def append_write(filename="", text=""):
    """Appends text to a filename
    Doesn't overwrite it because mode 'a'
    Create it if it doesn't exists"""
    with open(filename, mode="a", encoding="UTF8") as appender:
        appender.write(text)
        return len(text)
