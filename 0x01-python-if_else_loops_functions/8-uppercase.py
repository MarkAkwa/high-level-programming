#!/bin/python 

def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            x = chr(ord(i) - 32)
            print("{:s}".format(x), end="")
        else:
            print("{:s}".format(i), end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")
