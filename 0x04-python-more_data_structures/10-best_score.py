#!/usr/bin/python3
""" a function that returns a key with the biggest integer value. """


def best_score(a_dictionary):
    for key, value in a_dictionary.items():
        if len(list(a_dictionary)) == 0:
            return None
        else:
            while len(list(a_dictionary)):
                if value > value + 1:
                    return a_dictionary[key]
