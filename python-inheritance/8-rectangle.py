#!/usr/bin/python3
""" This module has the BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Initializes a new rectangle """
    def __init__(self, width, height):
        """ Init special method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
