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

print_last_digit(98) 
print_last_digit(0) 
print_last_digit(-1024) 
