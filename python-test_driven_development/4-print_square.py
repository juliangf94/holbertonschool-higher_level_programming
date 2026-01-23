#!/usr/bin/python3
"""
Module print_square
Prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The length of the square's side.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
