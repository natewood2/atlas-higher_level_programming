#!/usr/bin/python3
"""Defines a module that appends a string"""


def append_write(filename="", text=""):
    """Appending to the end of a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
