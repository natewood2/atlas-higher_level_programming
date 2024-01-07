#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_s = list(a_dictionary)
    list_s.sort()
    for key in list_s:
        print("{}: {}".format(key, a_dictionary[key]))
