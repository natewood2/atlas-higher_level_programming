#!/usr/bin/python3
""" Defines a class """


class Square:
    """ Defines a plan for square """
    def __init__(self, size=0):
        error_ = "size must be an integer"
        _error = "size must be >= 0"
        if not isinstance(size, int):
            raise TypeError(error_)
        if size < 0:
            raise ValueError(_error)
        self.__size = size
