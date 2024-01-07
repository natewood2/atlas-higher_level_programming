#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_diction = {}
    for key, value in a_dictionary.items():
        new_diction[key] = value * 2
    return new_diction
