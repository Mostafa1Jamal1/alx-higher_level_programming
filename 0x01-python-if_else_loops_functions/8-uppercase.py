#!/usr/bin/env python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            c = chr(ord(str[i]) - (ord('a') - ord('A')))
        else:
            c = str[i]
        print("{:s}".format(c), end="")
    print()
