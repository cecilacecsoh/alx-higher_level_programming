#!/usr/bin/python3

"""
function that writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation and 
    You don’t need to manage file permission exceptions"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
