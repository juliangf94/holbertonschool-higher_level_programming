#!/usr/bin/python3
"""
This module demonstrates the Mixin pattern by creating specialized
classes for swimming and flying, then combining them into a Dragon class.
"""


class SwimMixin:
    """
    Provides swimming functionality.
    """
    def swim(self):
        """
        Prints a swimming message.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Provides flying functionality.
    """
    def fly(self):
        """
        Prints a flying message.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that composes behaviors from SwimMixin and FlyMixin.
    """
    def roar(self):
        """
        Prints a roar message unique to the Dragon.
        """
        print("The dragon roars!")
