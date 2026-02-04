#!/usr/bin/python3
"""
Module defining a geometry class for basic operations.
The purpose of this module is to provide a foundation for
more specific geometric shapes like rectangles and squares.
"""


class BaseGeometry:
    """
    Representation of the base geometry class.
    This class serves as a blueprint for geometric calculations.
    """

    def area(self):
        """
        Computes the area of the geometry.
        This specific method is meant to be overridden in child classes.
        Raises an Exception because it is not yet implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a provided value is a strictly positive integer.
        Args:
            name: The string label for the integer value.
            value: The integer to be checked for validity.
        Raises:
            TypeError: if the value provided is not an integer.
            ValueError: if the value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
