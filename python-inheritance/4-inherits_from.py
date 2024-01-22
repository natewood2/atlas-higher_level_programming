#!/usr/bin/python3
""" Defines a module """


def inherits_from(obj, a_class):
    """function that returns True if the object is a subclass"""
    if type(obj) is a_class:
        return False

    return isinstance(obj, a_class)
