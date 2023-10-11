#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = 0
    max_key = None
    for k in a_dictionary:
        if a_dictionary[k] > maxval:
            max_val = a_dictionary[k]
            max_key = k
    return max_key
