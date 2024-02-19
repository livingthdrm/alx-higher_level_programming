#!/usr/bin/python3
""" a function that computes the square value of all integers of a matrix. """


def square_matrix_simple(matrix=[]):
    new_mat = []
    for row in matrix:
        new_row = []
        for item in row:
            result = item**2
            new_row.append(result)
        new_mat.append(new_row)
    return new_mat
