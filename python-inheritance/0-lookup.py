#!/usr/bin/python3
"""
This module provides a function to look up attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing attributes and methods.
    """
    return dir(obj)
