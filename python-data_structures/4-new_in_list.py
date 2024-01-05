#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_l = my_list.copy()

    if idx < 0 or  idx >= len(copy_l):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    
    return new_list
