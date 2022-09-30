#!/usr/bin/python3
"""Module 100 - Search and update baby"""


def append_after(filename="", search_string="", new_string=""):
    """ Function that insert a line of text
    to a file, after each line containing a
    specific string
        1- open the file
        2- add the lines which does'nt match
        3- if there's a match add the new_string after pattern
        4- overwrite the original file, for so use seek(0)
        to set the File Handle at the beginning 
        """
    with open(filename, mode="r+") as old:
        new_text = ""
        for lines in old:
            new_text += lines
            if search_string in lines:
                new_text += new_string
        old.seek(0)
        old.write(new_text)
