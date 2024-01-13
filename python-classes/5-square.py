#!/usr/bin/python3
""" Defines a class """


class Square:
    """ Defines a plan for square """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        error_ = "size must be an integer"
        _error = "size must be >= 0"
        if not isinstance(value, int):
            raise TypeError(error_)
        if value < 0:
            raise ValueError(_error)
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        if self.__size > 0:
            for row in range(0, self.__size):
                for colum in range(self.__size):
                    print("#", end="")
                print()
