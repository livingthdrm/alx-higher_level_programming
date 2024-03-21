#!/usr/bin/python3
""" an class
Square that defines a square """


class Square:
    """ a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification) """

    __size = 0

    def __init__(self, size=0):
        """ A method to initialize square
            here we also try handle type error and value error
            exceptions. """
        try:
            self.__size = size

            if type(self.__size) != int:
                except TypeError:
                    print("size must be an integer")
            elif self.__size < 0:
                except ValueError:
                    print("size must be >= 0")
