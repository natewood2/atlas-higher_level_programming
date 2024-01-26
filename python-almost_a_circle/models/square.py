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
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        num_of_args = len(args)

        if num_of_args > 0:
            if num_of_args >= 1:
                self.id = args[0]
            if num_of_args >= 2:
                self.size = args[1]
            if num_of_args >= 3:
                self.x = args[2]
            if num_of_args >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary Representation of Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
