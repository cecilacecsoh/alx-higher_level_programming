#!/usr/bin/python3

"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """it writes a string to a text file.
        Args:
            filename (str): the name of file.
            text (str): the text to be written.
            Return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        files = file.write(text)
        return (files)
