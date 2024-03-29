#!/usr/bin/python3
""" a function that prints x elements of a list. """


def safe_print_list(my_list=[], x=0):
    try:
        my_list = my_list[:x]
        for i, item in enumerate(my_list):
            print(item, end="")
        print()
        return i + 1
    except IndexError:
        print("Index out of range")
