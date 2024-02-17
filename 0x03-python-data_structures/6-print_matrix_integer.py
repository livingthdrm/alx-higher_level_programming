#!/usr/bin/python3
""" a function that prints a matrix of integers. """


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index,  item in enumerate(row):
            if index == (len(row) - 1):
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
        print()
