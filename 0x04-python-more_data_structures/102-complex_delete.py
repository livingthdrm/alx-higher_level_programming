#!/usr/bin/python3
""" a function that deletes keys with a specific value in a dictionary. """


def complex_delete(a_dictionary, value):
    for key, valued in a_dictionary.items():
        if value not in a_dictionary.values():
            return a_dictionary

    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]

    for key in keys_to_delete:
        del a_dictionary[key]

    if value in a_dictionary.values():
        complex_delete(a_dictionary, value)

    return a_dictionary
