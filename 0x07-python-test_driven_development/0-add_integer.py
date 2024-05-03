#!/usr/bin/python3
"""
a function that adds 2 integers
Prototype: def add_integer(a, b=98
Returns an integer: the addition of a and
"""


def add_integer(a, b=98):
    """ a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int):
        raise TypeError('b must be an integer')

    return (a + b)
