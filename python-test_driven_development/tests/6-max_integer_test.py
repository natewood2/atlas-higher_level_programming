#!/usr/bin/python3
""" Max integer test module """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Erm Testing Function """
    def testing_max_at_end(self):
        """ Testing max at end """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        
    def testing_max_at_beginning(self):
        """ Testing max at beginning """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        
    def testing_max_in_middle(self):
        """ Testing max in middle """
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
        
    def testing_with_one_int(self):
        """ Testing with one element """
        self.assertEqual(max_integer([4]), 4)
    
    def testing_with_the_same_int(self):
        """ Testing with same int """
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)
        
    def testing_with_none(self):
        """ Testing with none """
        self.assertEqual(max_integer([]), None)
        
    def testing_with_negative(self):
        """ Testing with negative """
        self.assertEqual(max_integer([-4, -5, -6, -7, -8]), -4)