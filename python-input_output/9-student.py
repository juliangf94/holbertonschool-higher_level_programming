#!/usr/bin/python3
"""
This module defines a Student class.
The class includes methods to represent the student as a dictionary.
"""


class Student:
    """
    Representation of a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance with specific attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary containing student attributes.
        """
        return self.__dict__
