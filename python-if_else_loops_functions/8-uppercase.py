#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for i in str:
        # ord used to find ASCII value
        if ord('z') >= ord(i) >= ord('a'):
            # chr used to find the character from ASCII value
            newstr += chr(ord(i) - 32)
        else:
            newstr += i
    print(newstr)
