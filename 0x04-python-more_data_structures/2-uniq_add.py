#!/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    new_list = set(my_list)
    for i in new_list:
        addition += i
    return addition


my_list = [1, 2, 3, 1, 4, 2, 5] 
result = uniq_add(my_list) 
print("Result: {:d}".format(result))
