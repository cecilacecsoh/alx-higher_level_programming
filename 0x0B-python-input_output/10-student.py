#!/usr/bin/python3

"""
class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """
        A class students that defines a student by:
        Attributes:
            first_name (str): fist student's name
            last_name (str): second student's name 
            age (int): age of student.
        Methods:
            __init__ - to initializes the Student instance.
            to_json - this retrieves dictionary repr of Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
            an initialisation of a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
           this  retrieves a dictionary representation of Student.
            Args:
                attr (list): An attribute names that are to be retrieved
        """

        if attr is not None:
            res = {n: self.__dict__[n] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
