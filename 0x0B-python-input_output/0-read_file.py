#!/usr/bin/python3

"""
a function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """""reads text file, then prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        files = file.read()
        print(files, end="")
