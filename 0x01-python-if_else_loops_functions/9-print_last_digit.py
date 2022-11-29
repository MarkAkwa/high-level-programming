#!/bin/python

def print_last_digit(num):
    t = " ".join(str(num))
    t = list(t)
    l = []
    for i in t:
        if i != " ":
            l.append(i)
        else:
            pass
    x = l.pop()
    print(x, end="")
