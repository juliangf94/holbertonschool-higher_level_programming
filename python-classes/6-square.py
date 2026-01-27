#!/usr/bin/python3
"""
This module defines a Square class with size and position properties.
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size lenth of the square (private)
        __position (tuple): The (x, y) coordinates of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
            position (tuple): The (x, y) coordinates of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position with specific validation for a tuple
        of two positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        #   Print vertical offset (y coordinate)
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")

        #   Print each row with horizontal offset (x coordinate)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
