#!/usr/bin/python3
"""Defines a square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class of the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Property"""
        self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size
