#!/usr/bin/python3
""" a class Square that defines a
square by: (based on 1-square.py) """


class Square:
    """ Private instance attribute: size

    Attributes:
        size of the square """
    def __init__(self, size=0):
        """ Initializing the square

        Attribute:
            size of square """

        self.__size = size

    @property
    def size(self):
        """ A method to retrieve the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ A setter method to set the size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")

        self.__size = value

    def area(self):
        """ A module that takes the size
        and returns the current square area """
        return self.__size * self.__size
