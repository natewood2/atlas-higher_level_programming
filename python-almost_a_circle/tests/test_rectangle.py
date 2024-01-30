#!/usr/bin/python3
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class.
    """
    def test_initialization(self):
        """ Tests proper initialization of rectangle dimensions. """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)


    def test_invalid_width(self):
        """ Tests response to invalid width input. """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_area(self):
        """ Tests area calculation. """
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -1)
        with self.assertRaises(TypeError):
            Rectangle(2, '3')

    def test_str(self):
        """ Tests string representation of the Rectangle class. """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_fail(self):
        """ Tests string representation if fails return TypeError. """
        with self.assertRaises(TypeError):
            Rectangle("is a number", 2)

    def test_is_other_str_fail(self):
        """ Tests if string representation if fails return TypeError. """
        with self.assertRaises(TypeError):
            Rectangle(2, "is another number")


    def test_base(self):
        """ Tests if Rectangle is a subclass of Base. """
        new = Rectangle(10, 10)
        self.assertEqual(True, isinstance(new, Base))

    def testing_display(self):
        """ Tests visual display output of the Rectangle. """
        r = Rectangle(3, 2, 2, 2)
        expected_output = "\n\n  ###\n  ###\n"
        r.display()
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

    def setUp(self):
        """ Prepares environment for tests by capturing print statements. """
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        """ Resets print statement capturing. """
        sys.stdout = sys.__stdout__

    def test_invalid_x_y(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(2, 3, 0, -1)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, '1', 0)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 3)
        self.assertEqual(r.to_dictionary(), {
            'id': 3, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

if __name__ == '__main__':
    unittest.main()
