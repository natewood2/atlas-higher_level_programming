#!/usr/bin/python3
""" Documenting module """


def print_square(size):
    """ Documention module """
    size_error = "size must be an integer"
    value_error = "size must be >= 0"
    float_and_zero_error = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(size_error)
    if size < 0:
        raise ValueError(value_error)
    if isinstance(size, float):
        raise TypeError(float_and_zero_error)

    print(("#" * size + '\n') * size, end='')
