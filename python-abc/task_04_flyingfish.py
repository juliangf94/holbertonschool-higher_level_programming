#!/usr/bin/python3
"""
This module explores multiple inheritance through Fish, Bird,
and the hybrid FlyingFish classes.
"""


class Fish:
    """
    Class representing a fish
    """
    def swim(self):
        """
        Prints swimming behavior.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird
    """
    def fly():
        """
        Prints flying behavior.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish, inheriting from both Fish and Bird.
    """
    def fly(self):
        """
        Overrides Bird's fly method.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Overrides Fish's swim method.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Overrides both parent habitat methods.
        """
        print("The flying fish lives both in water and the sky!")
