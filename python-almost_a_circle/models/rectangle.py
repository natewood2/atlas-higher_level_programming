#!/usr/bin/python3
"""Defines module for rect"""
from models.base import Base


class Rectangle(Base):
    """Rect class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width

        self.__height = height

        self.__x = x

        self.__y = y

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
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        self.__width = width

    @height.setter
    def height(self, height):
        """Defines setter"""
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__height = height

    @property
    def x(self):
        """Defines property"""
        return self.__x

    @x.setter
    def x(self, x):
        """Defines x"""
        if x <= 0:
            raise ValueError("x must be >= 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        self.__x = x

    @property
    def y(self):
        """Defines property"""
        return self.__y

    @y.setter
    def y(self, y):
        """Defines y setter"""
        if y <= 0:
            raise ValueError("y must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        self.__y = y
