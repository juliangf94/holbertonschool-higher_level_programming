#!/usr/bin/env python3
"""
Module for custom object serialization using pickle.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with basic attributes.
    """

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object in a specific format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, PermissionError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads an instance of CustomObject from a file.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None
