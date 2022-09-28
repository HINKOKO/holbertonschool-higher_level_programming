#!/usr/bin/python3
"""Module - 0 Read that file buddy!"""


def read_file(filename=""):
    """reads a text file and print to stdout"""
    with open(filename, encoding="UTF8") as worky:
        for line in worky:
            print(line, end="")
