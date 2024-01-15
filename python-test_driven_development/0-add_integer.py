#!/usr/bin/python3
""" Function that adds floats and ints """


def add_integer(a, b=98):
    """ Returns the addition or raises a type error depending on user input """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return a + b
