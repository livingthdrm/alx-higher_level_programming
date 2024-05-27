#!/usr/bin/python3
"""
    a function that prints My name is <first name> <last name>
    first_name and last_name must be strings otherwise,
    raise a TypeError exception
"""


def say_my_name(first_name, last_name=""):
    """ A function to output the first name and last name
    if any or all is not a string
    raise a TypeError exception """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
