#!/usr/bin/python3
""" a function that prints a square with the character #.

    Prototype: def print_square(size):
    size is the size length of the square
    """


def print_square(size):
    """
    size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
