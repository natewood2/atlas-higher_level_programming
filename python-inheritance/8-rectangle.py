#!/usr/bin/python3
""" Defines non empty class """


class BaseGeometry:
    """ Class raises a expects """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Class of rectangle """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height       
 