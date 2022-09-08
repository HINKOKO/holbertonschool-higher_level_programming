#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if (len(argv) < 2):
        print("Number of argument(s) {} argument:".format(len(argv)))
    else:
        print("Number of argument(s) {} arguments:".format(len(argv)))
for i, arg in enumerate(argv):
    print("{}: {}".format(i, arg))
