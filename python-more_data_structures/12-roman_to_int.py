#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0

    if not isinstance(roman_string, str):
        return 0

    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    updated_value = 0

    for c in reversed(roman_string):
        value = dict[c]
        if value < updated_value:
            num -= value
            updated_value = value
        else:
            num += value
        updated_value = value
    return num
