#!/usr/bin/python3
""" a function that prints x elements of a list. """


def safe_print_list(my_list=[], x=0):
    try:
        for i, item in enumerate(my_list):
            if i <= x:
                print(item)
                return i
    except IndexError:
        return 1
