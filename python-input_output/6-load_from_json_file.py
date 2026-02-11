#!/usr/bin/python3
"""
This module defines a function that creates an Object from a JSON file.
It uses the json module to deserialize file content.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        any: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
