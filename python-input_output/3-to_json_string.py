#!/usr/bin/python3
"""
This module defines a function that converts a Python object
to its JSON string representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The Python object to be serialized.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
