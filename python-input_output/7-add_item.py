#!/usr/bin/python3
"""Module 7 - Load, add, save
- script that adds all argument to a Python list
- and save them to a file: "add_item.json"
We load from add_item.json if some content exists
otherwise it is initialized at line 15 - empty list
Then it is added and saved"""
from sys import argv
# to retrieve the arguments on command line after script
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_expected = "add_item.json"

try:
    file_content = load_from_json_file(file_expected)
except FileNotFoundError:
    file_content = []

save_to_json_file(file_content + argv[1:], "add_item.json")
