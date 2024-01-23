#!/usr/bin/python3
"""Module that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writing an object to a text file"""
    return json.dump(my_obj, filename)
