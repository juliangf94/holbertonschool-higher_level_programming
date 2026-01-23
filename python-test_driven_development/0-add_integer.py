#!/usr/bin/python3
"""
Module that provides a function to add two integers.
"""
def add_integer(a, b=98):
    """
    Adds to integers and returns the result.

    a and b must be integers or floats.
    If they are floats, they are first casted to integers.
    Othervise, a TypeError is raised.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
