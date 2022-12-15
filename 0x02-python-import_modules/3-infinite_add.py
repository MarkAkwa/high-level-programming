#!/bin/python
from sys import argv

incr = 0
length = len(argv)
for i in range(1, length):
    incr += int(argv[i])

print('{}'.format(incr))
