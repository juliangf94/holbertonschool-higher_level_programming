#!/usr/bin/python3
"""
This module contains the function pascal_triangle.
It generates a Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle as a list of lists.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Start the new row with 1
        new_row = [1]

        # Calculate the numbers between the 1s
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        # End the new row with 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle
