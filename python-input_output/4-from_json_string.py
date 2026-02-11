#!/usr/bin/python3
"""
This module defines a function that converts a JSON string
into a Python data structure.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        any: The Python object (list, dict, str, etc.).
    """
    return json.loads(my_str)
