#!/usr/bin/python3
""" a function that deletes a key in a dictionary. """


def simple_delete(a_dictionary, key=""):
    if key not in list(a_dictionary):
        return a_dictionary
    else:
        del a_dictionary[key]

    return a_dictionary
