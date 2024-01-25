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
    def width(self, value):
        """defines setter"""
        if value <= 0:
            raise ValueError("Value needs to be greater than 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Defines setter"""
        if value <= 0:
            raise ValueError("Value needs to be greater than 0")
        self.__height = value
    
    @property
    def x(self):
        """Defines property"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Defines x"""
        if value <= 0:
            raise ValueError("Value needs to be greater than 0")
        self.__x = value
  
    @property
    def y(self):
        """Defines property"""
        return self.__y

    @y.setter
    def y(self, value):
        """Defines y setter"""
        if value <= 0:
            raise ValueError("Value needs to be greater than 0")
        self.__y = value