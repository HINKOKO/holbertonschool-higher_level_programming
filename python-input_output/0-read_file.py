#!/usr/bin/python3
"""Module - 0 Read that file buddy!"""


def read_file(filename=""):
    """reads a text file and print to stdout"""
    with open(filename, 'r', encoding="UTF-8") as worky:
        print(worky.read())
