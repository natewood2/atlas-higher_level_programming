#!/usr/bin/python3
import unittest
import io
import sys
from models.square import Square
from models.base import Base
""" Unit test for Square Class. """


class TestSquare(unittest.TestCase):
    """ Beginning Tests for Square. """
    def test_init(self):
        """Test Square initialization."""
        square = Square(5, 2, 3, 10)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 10)

    def test_invalid_size(self):
        """ Tests response to invalid size input. """
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(TypeError):
            Square('3')

    def test_area(self):
        """ Tests area calculation. """
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_with_two(self):
        """ Testing with two. """
        square = Square(3, 4)
        self.assertEqual(square.area(), 12)

    def test_str(self):
        """ Tests string representation of the Square class. """
        square = Square(4, 2, 1, 12)
        self.assertEqual(str(square), "[Square] (12) 2/1 - 4")

    def test_str_fail(self):
        """ Tests string representation if fails return TypeError. """
        with self.assertRaises(TypeError):
            Square("is a number")

    def test_is_other_str_fail(self):
        """ Tests if string representation if fails return TypeError. """
        with self.assertRaises(TypeError):
            Square("is another number")

    def test_base(self):
        """ Tests if Square is a subclass of Base. """
        new_square = Square(10)
        self.assertEqual(True, isinstance(new_square, Base))

    def test_size_property(self):
        """ Test the size property. """
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        """ Test the size setter. """
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update(self):
        """ Test the update method. """
        square = Square(5)
        square.update(10, 15, 20, 25)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 25)
        square.update(size=30, y=35)
        self.assertEqual(square.size, 30)
        self.assertEqual(square.y, 35)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        square = Square(5, 2, 3, 10)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
