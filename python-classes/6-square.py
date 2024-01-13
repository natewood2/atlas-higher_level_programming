#!/usr/bin/python3
""" Defines a class """


class Square:
    """ Defines a plan for square """
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for row in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
