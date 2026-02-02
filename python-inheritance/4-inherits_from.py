#!/usr/bin/python3
"""
This module contains a function to vertify if an object is an instance of
a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj inherited from a_class and is not an exact instance
        of a_class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
