#!/usr/bin/python3
""" a function that computes the square value of all integers of a matrix. """


def square_matrix_simple(matrix=[]):
    #new_mat = ((lambda x: x**2) for row in matrix for x in row)
    #return new_mat
    new_mat = []
    for row in matrix:
        for i in row:
            result = i**2
        new_mat.append(result)
    return new_mat
