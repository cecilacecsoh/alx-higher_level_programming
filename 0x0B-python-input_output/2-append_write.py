#!/usr/bin/python3

"""
a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ it appends a string and returns the number of characters added
    If the file doesn’t exist, it should be created"""
    with open(filename, "a", encoding="utf-8") as file:
        lines = file.write(text)
        return lines
