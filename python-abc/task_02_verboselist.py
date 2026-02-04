#!/usr/bin/env python3
"""
This module defines the VerboseList class which extends the built-in list.
It provides notifications when items are added or removed.
"""


class VerboseList(list):
    """
    A custom list class that prints a message when modified.
    """

    def append(self, item):
        """
        Adds an item and prints a notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extends the list and prints a notification with the count.
        """
        item_count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(item_count))

    def remove(self, item):
        """
        Prints a notification and removes an item.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Prints a notification and pops an item.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
