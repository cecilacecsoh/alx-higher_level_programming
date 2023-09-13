#!/usr/bin/python3
"""
A function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """ the method for inserting text after search string."""
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        n = 0
        while n < len(lines):
            if search_string in lines[n]:
                lines[n:n + 1] = [line[n], new_string]
                n += 1
            n += 1
 
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
