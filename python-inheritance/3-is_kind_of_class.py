#!/usr/bin/python3
"""
This module contains a function to vertify if an object is an instance of,
or inherited from, a specific class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance or inherited from a_class;
        otherwise False.
    """
    return isinstance(obj, a_class)
