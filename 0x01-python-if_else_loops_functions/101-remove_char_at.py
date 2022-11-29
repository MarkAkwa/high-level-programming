#!/bin/python

def remove_cha_at(str, n):
    if n >= 0:
        str = str[:n] + str[n + 1:]
    return str

print(remove_cha_at("hello world", 4))
