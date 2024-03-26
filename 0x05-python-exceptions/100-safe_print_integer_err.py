#!/usr/bin/python3
"""a function that prints an integer """


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as err:
        print("Exception: {}".format(err), file=sys.stderr)
