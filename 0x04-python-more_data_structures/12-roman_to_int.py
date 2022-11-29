#!/bin/python3
def roman_to_int(roman_string):
        roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        item = 0
        roman = roman_string
        if type(roman) != str or len(roman) == 0:
                return 0
        for i in range(item, len(roman)):
                if item < len(roman) - 1 and roman_dictionary[roman[item]] < roman_dictionary[roman[item + 1]]:
                    result -= roman_dictionary[roman[item]]
                else:
                    result += roman_dictionary[roman[item]]
        return result


roman_number = "X" 
print("{} = {}".format(roman_number, roman_to_int(roman_number))) 
 
roman_number = "VII" 
print("{} = {}".format(roman_number, roman_to_int(roman_number))) 
 
roman_number = "IX" 
print("{} = {}".format(roman_number, roman_to_int(roman_number))) 
 
roman_number = "LXXXVII" 
print("{} = {}".format(roman_number, roman_to_int(roman_number))) 
 
roman_number = "DCCVII" 
print("{} = {}".format(roman_number, roman_to_int(roman_number))) 

