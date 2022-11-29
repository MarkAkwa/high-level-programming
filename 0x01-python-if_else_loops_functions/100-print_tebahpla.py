#!/bin/python

i = 122
while i >= 97:
    flag = 0
    if i % 2 != 0:
        i -= 32
        flag = 1
    print("{:s}".format(chr(i)), end="")
    if flag == 1:
        i += 32
    i -= 1