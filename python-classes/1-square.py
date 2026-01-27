#!/usr/bin/python3
"""
This module defines a square class.
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size length of the square (private)
    """
    def __init__(self, size):
        """
        Initialize the square with a specific size

        Args:
            size: The size of the square´s side.
        """
        self.__size = size
