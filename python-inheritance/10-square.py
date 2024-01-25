#!/usr/bin/python3
"""Module contains and inherits from 9-rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defining new rectangle class"""
    def __init__(self, size):
        """ Init method """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
