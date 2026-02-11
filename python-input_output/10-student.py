#!/usr/bin/python3
"""
This module defines a Student class with attribute filtering.
It allows converting the object to a dictionary with specific keys.
"""


class Student:
    """
    Representation of a student with filtering capabilities.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student.
        If attrs is a list of strings, only those attributes are included.

        Args:
            attrs (list): A list of strings representing attribute names.

        Returns:
            dict: The filtered or full dictionary of the student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for a in attrs:
                if a in self.__dict__:
                    res[a] = self.__dict__[a]
            return res
        return self.__dict__
