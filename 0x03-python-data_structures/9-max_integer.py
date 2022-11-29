#!/bin/python

def max_integer(my_list=[]):
    highest = 0
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if i > highest:
                highest = i

        if highest == 0:
            return(my_list[0])
        else:
            return highest
    # if my_list is None or len(my_list) == 0:
    #     return None
    # largest = my_list[0]
    # for num in my_list:
    #     if num > largest:
    #         largest = num
    # return largest
my_list = [1, 90, 2, 13, 34, 5, -13, 3] 
max_value = max_integer(my_list) 
print("Max: {}".format(max_value))
