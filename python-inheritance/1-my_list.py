#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that provides a method to print sorted elements.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements are integers.
        """
        print(sorted(self))
