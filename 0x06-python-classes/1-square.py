#!/usr/bin/python3
""" an class
Square that defines a square """


class Square:
    """ a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification) """

    __size = 0

    def __init__(self, size):
        """ A method to initialize square """
        self.__size = size
