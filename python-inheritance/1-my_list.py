#!/usr/bin/python3
""" Defines a module """


class MyList(list):
    """ Defines a class """
    def print_sorted(self):
        """ prints sorting in order """
        print(sorted(self))