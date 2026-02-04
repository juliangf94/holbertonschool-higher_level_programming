#!/usr/bin/env python3
"""
This module defines the Shape abstract class and its subclasses,
Circle and Rectangle, to demonstrate duck typing and interfaces.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class defining the blueprint for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle.
    """
    def __init__(self, radius):
        """
        Initializes the circle with a radius.
        """
        self.radius = radius

    def area(self):
        """Returns the area of the circle: pi * r^2"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle: 2 * pi * r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """Returns the area: width * height"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter: 2 * (width + height)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Standalone function that uses Duck Typing to print
    information about any object that has area and perimeter methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
