#!/bin/python

import random

randomizer = random.randint(-100, 100)

def checker(x):
    if x < 0:
        print(f'{x} is negative')
    elif x > 0:
        print(f'{x} is positive')
    else:
        print(f'{x} is zero')

checker(randomizer)
