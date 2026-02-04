#!/usr/bin/python3
"""
This module defines the CountedIterator class.
It wraps an iterator to keep track of how many items have been processed.
"""


class CountedIterator:
    """
    An iterator wrapper that counts the number of items iterated.
    """
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated.

        Returns:
            int: The iteration count.
        """
        return self.count

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.

        Raises:
            StopIteration: If there are no more items to iterate.

        Returns:
            The next item from the sequence.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
