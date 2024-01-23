#!/usr/bin/python3
"""Creating a obj from json module"""
import json


def load_from_json_file(filename):
    """creating a obj"""
    with open(filename, 'r') as json_file:
        return json.load(json_file)
