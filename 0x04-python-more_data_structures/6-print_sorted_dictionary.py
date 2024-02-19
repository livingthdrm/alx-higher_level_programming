#!/usr/bin/python3
""" a function that prints a dictionary by ordered keys. """


def print_sorted_dictionary(a_dictionary):
    for keys, values in sorted(a_dictionary.items()):
        print("{} : {}".format(keys, values))