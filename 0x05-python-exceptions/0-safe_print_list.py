#!/usr/bin/python3
""" a function that prints x elements of a list. """


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x + 1):
            print(my_list[i], end="")
            return i + 1
    except IndexError:
        return 1
