import unittest
import sys
import os
import json
from models.base import Base
from models.rectangle import Rectangle
""" Unit Test for Base Class. """


class TestBase(unittest.TestCase):

    def setUp(self):
        """ Setup that is needed. """
        Base._Base__nb_objects = 0

    def test_init(self):
        """ Testing __init__. """
        base_class = Base()
        self.assertEqual(base_class.id, 1)

    def test_to_json_string(self):
        """ Takes a list of dictionaries and returns a JSON string. """
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_json_string(self):
        """ Takes a JSON string and returns a list of dictionaries. """
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file(self):
        """ Testing the save_to_file method. """
        rect1 = Rectangle(1, 2, 1)
        rect2 = Rectangle(3, 4, 2)
        Rectangle.save_to_file([rect1, rect2])
        filename = "Rectangle.json"
        self.assertTrue(os.path.isfile(filename))
        with open(filename, "r") as file:
            contents = json.loads(file.read())
            self.assertEqual(len(contents), 2)
        os.remove(filename)

    def test_create(self):
        """ Test the create method. """
        attributes = {'id': 35, 'width': 2, 'height': 3}
        rect = Rectangle.create(**attributes)
        self.assertEqual(rect.id, 35)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)

    def test_load_from_file(self):
        """ Test the load_from_file method. """
        r1 = Rectangle(1, 2, 1)
        r2 = Rectangle(3, 4, 2)
        Rectangle.save_to_file([r1, r2])
        rect_list = Rectangle.load_from_file()
        self.assertEqual(len(rect_list), 2)
        self.assertEqual(rect_list[0].id, 1)
        self.assertEqual(rect_list[1].id, 2)
        os.remove("Rectangle.json")

    def tearDown(self):
        """ Clean up code. """
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
