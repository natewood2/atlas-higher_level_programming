#!/usr/bin/python3
"""Defines modules that opens a file and reads from it"""


def read_file(filename=""):
    """Defining function"""
    with open(filename, 'r', encoding='utf-8') as f:
        for file in f:
            print(file, end='')
