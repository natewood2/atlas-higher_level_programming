#!/usr/bin/python3
import json
"""JSON representation"""


def to_json_string(my_obj):
    """JSON representation of obj"""
    with open('output.json', 'w') as json_file:
        json.dump(my_obj)
