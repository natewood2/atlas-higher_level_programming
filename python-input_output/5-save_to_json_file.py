#!/usr/bin/python3
"""Module that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writing an object to a text file"""
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)
