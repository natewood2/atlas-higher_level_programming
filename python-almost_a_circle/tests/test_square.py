#!/usr/bin/python3
import unittest
import io
import sys
import os
import json
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

    def test_square_1_and_2(self):
        """ Test creation of Square with size 1 and x 2. """
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)
        self.assertIsInstance(square.id, int)

    def test_invalid_x(self):
        """ Testing a invalid x parameter. """
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_invalid_y(self):
        """ Testing invalid y parameter. """
        with self.assertRaises(TypeError):
            Square("1", 2)

    def test_invalid_with_three(self):
        """ Testing a invalid x parameter. """
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_negative_x(self):
        """ Testing negative x parameter. """
        with self.assertRaises(ValueError):
            Square(2, -1)

    def test_negative_y(self):
        """ Testing negative y parameter. """
        with self.assertRaises(ValueError):
            Square(-1, 2)

    def test_negative_with_three(self):
        """ Testing negative y parameter. """
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_with_zero(self):
        """ Testing square with zero. """
        with self.assertRaises(ValueError):
            Square(0)

    def test_save_to_file_(self):
        """ Test Rectangle.save_to_file with None. """
        Square.save_to_file(None)
        filename = "Square.json"

        self.assertTrue(os.path.isfile(filename))

        with open(filename, "r") as file:
            contents = file.read()
            self.assertEqual(contents, "[]")

        os.remove(filename)

    def test_save_to_file_save(self):
        """ Test Rectangle.save_to_file with None. """
        Square.save_to_file([])
        filename = "Square.json"

        self.assertTrue(os.path.isfile(filename))

        with open(filename, "r") as file:
            contents = file.read()
            self.assertEqual(contents, "[]")

        os.remove(filename)

    def test_to_dictionary(self):
        r = Square(2, 1, 9, 3)
        self.assertEqual(r.to_dictionary(), {
            'id': 3, 'size': 2, 'x': 1, 'y': 9})

    def testing_id(self):
        """ Testing id. """
        square = Square.create(id=89)

        self.assertEqual(square.id, 89)

    def test_save_to_file_save_2(self):
        """ Test Rectangle.save_to_file with None. """
        Square.save_to_file([Square(1)])
        filename = "Square.json"

        self.assertTrue(os.path.isfile(filename))

        with open(filename, "r") as file:
            contents = json.loads(file.read())
            self.assertEqual(len(contents), 1)
            self.assertEqual(contents[0]['size'], 1)

        os.remove(filename)

    def test_load_from_file_no_file(self):
        """ Testing when file doesn't exist. """
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_when_it_does_exist(self):
        """ Testing when file exists. """
        Square.save_to_file([Square(1)])
        result = Square.load_from_file()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Square)
        self.assertEqual(result[0].size, 1)

        os.remove("Square.json")

if __name__ == '__main__':
    unittest.main()
