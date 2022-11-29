#!/bin/python

def no_c(my_string):
    x = []
    for i in my_string:
        if i != 'C' and i != 'c':
            x.append(i)
            
    return (''.join(x))
