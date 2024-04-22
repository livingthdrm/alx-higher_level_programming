#!/usr/bin/python3
""" a class Square that defines a
square by: (based on 1-square.py) """


class Square:
    """ Private instance attribute: size

    Attributes:
        size of the square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializing the square

        Attribute:
            size: size of each side of square
            psoition: position it is at """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ a method to retrieve the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ a setter method for the position attribute """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for val in value:
            if not isinstance(val, int) or val < 0:
                raise TypeError("position must be a \
                        tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ A module that takes the size
        and returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end='')

            print("#" * self.__size)

