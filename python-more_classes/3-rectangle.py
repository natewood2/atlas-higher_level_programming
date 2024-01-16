#!/usr/bin/python3
""" Defines a rectangle module """


class Rectangle():
    """ Defines the rectangle class """

    def __init__(self, width=0, height=0):
        """ Attributes for the rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Makes __width private also the gettor """
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ gettor of the height """
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ Area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter of rectangle """
        if self.width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ print the rectangle with the character #: """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for i in range(self.height):
            rectangle += "#" * self.width
            if i < self.height - 1:
                rectangle += "\n"
        return rectangle
            