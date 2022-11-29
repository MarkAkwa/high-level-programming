#!/bin/python

for i in range(0,100):
    if i == 99:
        print(f"{i} ",end="")
        break
    else:
        print("%02d" % i, sep=", ", end=", ")
