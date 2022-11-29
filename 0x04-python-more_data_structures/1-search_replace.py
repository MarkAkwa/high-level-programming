#!/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        if i == search:
            new.append(replace)
        else:
            new.append(i)
    return new


my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89] 
new_list = search_replace(my_list, 2, 89) 
 
print(new_list) 
print(my_list)
