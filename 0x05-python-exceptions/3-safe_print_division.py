#!/usr/bin/python3
""" a function that divides 2 integers and prints the result. """


def safe_print_division(a, b):
    try:
        result = 0
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
