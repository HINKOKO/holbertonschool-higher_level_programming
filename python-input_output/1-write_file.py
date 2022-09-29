#!/usr/bin/python3
"""Module - 1  Write to a friend
or a file it's better"""


def write_file(filename="", text=""):
    """opens and write a string 'text'
    to a file 'filename'"""
    with open(filename, mode='w', encoding="UTF8") as writty:
        writty.write(text)
        return writty.tell()
