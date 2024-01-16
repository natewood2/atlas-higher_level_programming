#!/usr/bin/python3
""" Defines a rectangle module """


class Rectangle():
    """ Defines the rectangle class """

    width_error = "width must be an integer"
    width_value_error = "width must be >= 0"
    height_error = "height must be an integer"
    height_value_error = "height must be >= 0"
    
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
                raise ValueError(width_value_error)
        else:
            raise TypeError(width_error)
    
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
                raise ValueError(height_value_error)
        else:
            raise TypeError(height_error)