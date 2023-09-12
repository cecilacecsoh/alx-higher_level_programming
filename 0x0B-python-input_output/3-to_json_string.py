#!/usr/bin/python3

"""
a function that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """returns the JSON and You don’t need to manage
    exceptions if the object can’t be serialized."""
    return json.dumps(my_obj)
