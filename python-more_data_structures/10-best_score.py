#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_num = 0
    max_val = None

    for key, value in a_dictionary.items():
        if value > max_num:
            max_num = value
            max_val = key
    return max_val
