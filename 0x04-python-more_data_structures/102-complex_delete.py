#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = []
    for k, v in a_dictionary.items():
        if value is v:
            new_list.append(k)
    if len(new_list) > 0:
        for new in new_list:
            del a_dictionary[new]
    return a_dictionary


print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary
a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]} 
new_dict = complex_delete(a_dictionary, 'C') 
print_sorted_dictionary(a_dictionary) 
print("--") 
print_sorted_dictionary(new_dict) 
 
print("--") 
print("--") 
new_dict = complex_delete(a_dictionary, 'c_is_fun') 
print_sorted_dictionary(a_dictionary) 
print("--") 
print_sorted_dictionary(new_dict)
