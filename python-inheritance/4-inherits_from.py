#!/usr/bin/python3
""" Defines a module """


def inherits_from(obj, a_class):
    """  a function that returns True if the object is an instance of a subclass """
    if type(obj) is a_class:
        return False
    
    return isinstance(obj, a_class)
