#!/usr/bin/python3

"""
a class Student that defines a student
"""


class Student:
    """ A representation of a student"""
    def __init__(self, first_name, last_name, age):
        """it initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return: Dictionary representation of student
        Public instance attributes"""
        return self.__dict__
