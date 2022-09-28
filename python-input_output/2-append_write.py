#!/usr/bin/python3
"""Module 2 - Append to a file"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="UTF8") as appender:
        appender.write(text)
        return len(text)
