#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            upper_str += char(ord(str) - 32)
        else:
            upper_str += char
    print(upper_str, end="")
    print()
