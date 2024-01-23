#!/usr/bin/python3
"""that writes a string to a text file"""


def write_file(filename="", text=""):
    """ Opening a file and returns the amount of Char"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return (len(text))
