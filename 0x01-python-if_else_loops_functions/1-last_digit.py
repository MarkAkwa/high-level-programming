#!/bin/python

import random

number = random.randint(-10000, 10000)

def check_last_number(num):
    t = " ".join(str(num))
    t = list(t)
    l = []
    for i in t:
        if i != " ":
            l.append(i)
        else:
            pass
    def greater_than (num):
        if num > 5:
            return " and is greater than 5"
        elif num == 0:
            return " and is 0"
        elif num < 6 and num != 0:
            return " and is less than 6 and not 0 "
        else:
            return " :) "

    print(f'Last digit of {num} is {i}{greater_than(int(i))}')

check_last_number(number)
