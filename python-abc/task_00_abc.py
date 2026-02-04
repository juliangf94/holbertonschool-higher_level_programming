#!/usr/bin/env python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
It demonstrates the use of Abstract Base Classes (ABC) to enforce method
implementation in derived classes.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an Animal.
    Cannot be instantiated directly.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        Returns:
            The sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a Dog.
    """
    def sound(self):
        """
        Implementation of the sound method for a Dog.
        Returns:
            str: The string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a Cat.
    """
    def sound(self):
        """
        Implementation of the sound method for a Cat.
        Returns:
            str: The string "Meow".
        """
        return "Meow"
