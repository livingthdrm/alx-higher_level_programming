#!/usr/bin/python3
""" a function that deletes keys with a specific value in a dictionary. """


def complex_delete(a_dictionary, value):
    for key, valued in a_dictionary.items():
        if value not in a_dictionary.values():
            return a_dictionary
        else:
            if value == valued:
                del a_dictionary[key]
    return a_dictionary
