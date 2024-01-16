#!/usr/bin/python3
""" Defines a module """
def text_indentation(text):
    """ Defines function """
    text_error = "text must be a string"
    
    if not isinstance(text, str):
        raise TypeError(text_error)
    
    empty_str = ""
    
    for each_char in text:
        if each_char in ['.', '?', ':']:
            empty_str = empty_str + each_char
            trimmed_str = empty_str.strip()
            print(trimmed_str)
            print("\n")
            empty_str = ""
        else:
            empty_str = empty_str + each_char