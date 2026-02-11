#!/usr/bin/python3
"""
This module defines a function for reading a text file.
It contains the read_file function which handles UTF-8 encoding.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
