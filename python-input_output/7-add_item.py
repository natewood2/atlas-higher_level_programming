#!/usr/bin/python3
"""Saves files module"""


import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""Adds everything to empty list"""
empty_list = []
list_of_arguments = sys.argv[1:]
if os.path.exists("add_item.json"):
    empty_list = load_from_json_file("add_item.json")
save_to_json_file(empty_list + list_of_arguments, "add_item.json")
