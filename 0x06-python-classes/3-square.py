#!/usr/bin/python3
""" a class Square that defines a
square by: (based on 1-square.py) """


class Square:
    """ Private instance attribute: size

    Attributes:
        size of the square """
    def __init__(self, size=0):
        """ size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer

            Args:
                if size is less than 0, raise a ValueError exception
                with the message size must be >= 0 """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ A module that takes the size
        and returns the current square area """
        return self.__size * self.__size
