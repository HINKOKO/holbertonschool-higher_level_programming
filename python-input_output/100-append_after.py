#!/usr/bin/python3
"""Module 100 - Search and update baby"""


def append_after(filename="", search_string="", new_string=""):
    """ Function that insert a line of text
    to a file, after each line containing a
    specific string"""
    with open(filename, mode="r+") as old:
        new_text = ""
        for lines in old:
            new_text += lines
            if search_string in lines:
                new_text += new_string
        old.write(new_text)
