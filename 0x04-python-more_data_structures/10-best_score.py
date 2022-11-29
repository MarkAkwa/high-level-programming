#!/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j is max(a_dictionary.values()):
                return i
    else:
        return None
