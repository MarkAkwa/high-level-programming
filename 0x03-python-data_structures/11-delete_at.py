#!/bin/python

def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    else:
        return my_list
    return my_list


my_list = [1, 2, 3, 4, 5] 
idx = 3 
new_list = delete_at(my_list, idx) 
print(new_list) 
print(my_list) 