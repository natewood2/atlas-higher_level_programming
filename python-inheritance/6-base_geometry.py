#!/usr/bin/python3
""" Defines non empty class """


class BaseGeometry:
    """ Class raises a expects """
    def area(self):
        raise Exception("area() is not implemented")
