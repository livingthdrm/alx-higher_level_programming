#!/usr/bin/python3
""" a function that prints x elements of a list. """


def safe_print_list(my_list=[], x=0):
    my_list = my_list[:x]
    try:
        for i, item in enumerate(my_list):
            if i < x:
                print(item, end='')
        print()
        return i + 1
    except IndexError:
        return i + 1
