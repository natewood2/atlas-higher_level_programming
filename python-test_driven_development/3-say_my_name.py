#!/usr/bin/python3
""" Documenting module """


def say_my_name(first_name, last_name=""):
    """ Say my name documentation """
    first_name_error = "first_name must be a string"
    last_name_error = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(first_name_error)
    if not isinstance(last_name, str):
        raise TypeError(last_name_error)
    full_name = first_name + " " + last_name

    print(f"My name is {full_name}")
