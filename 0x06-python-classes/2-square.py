#!/usr/bin/python3
""" a class Square that defines a 
square by: (based on 1-square.py) """


class Square:
    """ Private instance attribute: size
    You are not allowed to import any module"""

    __size = 0

    def __init__(self, size=0):
        """ Instantiation with optional size: def __init__(self, size=0):
            size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer


            if size is less than 0, raise a ValueError exception
            with the message size must be >= 0"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
