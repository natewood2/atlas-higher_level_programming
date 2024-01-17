#!/usr/bin/python3
""" Defines a module """


def text_indentation(text):
    """ Defines function """
    text_error = "text must be a string"

    if not isinstance(text, str):
        raise TypeError(text_error)

    empty_str = ""

    for each_char in text:
        empty_str = empty_str + each_char
        if each_char in ['.', '?', ':']:
            print(empty_str.strip())
            print()
            empty_str = ""
    if empty_str.strip():
        print(empty_str.strip(), end="")
