#!/bin/python

for i in range(ord('a'), ord('z') + 1):
    if i in (ord('e'), ord('q')):
        continue
    print('{:c}'.format(i), sep="", end="")
