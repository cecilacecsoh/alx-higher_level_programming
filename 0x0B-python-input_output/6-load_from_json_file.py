#!/usr/bin/python3

"""
function that creates an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file" You don’t need to manage;
    file permissions / exceptions and exceptions if the JSON
    string doesn’t represent an object."""
    with open(filename, 'r', encoding='utf-8') as file:
        create_obj = json.load(file)
        return create_obj
