#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    A class used to represent geometry
    """
    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Always, because it is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
