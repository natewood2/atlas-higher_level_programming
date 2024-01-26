#!/usr/bin/python3
"""Defines module for rect"""
from models.base import Base


class Rectangle(Base):
    """Rect class that inherits from Base"""

    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        """Defines property"""
        return self.__width

    @property
    def height(self):
        """Defines property"""
        return self.__height

    @width.setter
    def width(self, width):
        """defines setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Defines setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Defines property"""
        return self.__x

    @x.setter
    def x(self, x):
        """Defines x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Defines property"""
        return self.__y

    @y.setter
    def y(self, y):
        """Defines y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Defines the area"""
        return self.__width * self.__height

    def display(self):
        """Displays the #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + str(self.print_symbol) * self.width)

    def __str__(self):
        """Overriding"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        num_of_args = len(args)
        if num_of_args >= 1:
            self.id = args[0]
        if num_of_args >= 2:
            self.width = args[1]
        if num_of_args >= 3:
            self.height = args[2]
        if num_of_args >= 4:
            self.x = args[3]
        if num_of_args >= 5:
            self.y = args[4]

        for key, value, in kwargs.items():
            setattr(self, key, value)
            
    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
