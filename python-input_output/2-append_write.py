#!/usr/bin/python3
"""
This module defines a function that appends a string to a text file.
It returns the number of characters added during the operation.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
