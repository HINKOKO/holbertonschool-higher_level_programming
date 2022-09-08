#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if (len(argv) < 2):
        print("{} argument:".format(len(argv)))
    else:
        print("{} arguments:".format(len(argv)))
for i, arg in enumerate(argv):
    print("{}: {}".format(i, arg))
