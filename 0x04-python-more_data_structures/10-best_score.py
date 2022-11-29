#!/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j is max(a_dictionary.values()):
                return i
    else:
        return None


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10} 
best_key = best_score(a_dictionary) 
print("Best score: {}".format(best_key)) 
 
best_key = best_score(None) 
print("Best score: {}".format(best_key))
