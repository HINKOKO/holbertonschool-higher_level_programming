#!/usr/bin/python3
def uppercase(str):
    for i in str:
        # ord used to find ASCII value
        if ord('z') >= ord(i) >= ord('a'):
            # chr used to find character from an ASCII value
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end='')
    print('')
