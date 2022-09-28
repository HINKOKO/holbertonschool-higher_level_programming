#!/usr/bin/python3
"""Module - 0 Read that file buddy!"""


def read_file(filename=""):
    with open(filename, 'r', encoding="UTF-8") as fabien:
        print(fabien.read())
