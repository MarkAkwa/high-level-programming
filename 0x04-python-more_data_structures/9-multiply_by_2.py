#!/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i in a_dictionary:
        new[i] *= 2
    return new


multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2 
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary 
 
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16} 
new_dict = multiply_by_2(a_dictionary) 
print_sorted_dictionary(a_dictionary) 
print("--") 
print_sorted_dictionary(new_dict)  
