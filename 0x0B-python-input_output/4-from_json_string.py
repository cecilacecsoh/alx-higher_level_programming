#!/usr/bin/python3

"""
a function that returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """ it returns an object represented by a JSON string.You dont need to
    manage exceptions if the JSON string doesn’t represent an object"""
    return json.loads(my_str)
