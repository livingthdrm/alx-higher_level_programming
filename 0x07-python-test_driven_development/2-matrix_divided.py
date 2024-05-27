#!/usr/bin/python3
""" a function that divides all elements of a matrix.

    Prototype:
     def matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix.
    All elements of the matrix should be divided by div, rounded to 2 decimals
    Returns a new matrix """

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    first_row = len(matrix[0])
    for row in matrix:
        if len(row) != first_row:
            raise TypeError("Each row of the matrix must have the same size")
    if (not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(el, (int, float))
                    for row in matrix for el in row)):
        raise TypeError(msg)

    matrix2 = []
    for row in matrix:
        result = []
        for column in row:
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                result.append(round(column / div, 2))
        matrix2.append(result)
    return matrix2
