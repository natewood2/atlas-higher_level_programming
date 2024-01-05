#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_l = my_list.copy()

    if 0 < idx <= len(copy_l):
        copy_l[idx] = element

        return copy_l
