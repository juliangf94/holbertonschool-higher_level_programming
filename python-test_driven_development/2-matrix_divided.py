#!/usr/bin/python3
"""Module that provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): divisor

    Returns:
        list of lists: new matrix with divided values

    Raises:
        TypeError: if matrix is invalid or div is not a number
        ZeroDivisionError: if div is zero
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)
    row_size = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err_msg)
    return [[round(x / div, 2) for x in row] for row in matrix]
