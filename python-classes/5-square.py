#!/usr/bin/python3
"""
This module defines a square class with printing capabilities.
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size lenth of the square (private)
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The side of the length.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size if the square with validation.

        Args:
            value (int): The new side length.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)
