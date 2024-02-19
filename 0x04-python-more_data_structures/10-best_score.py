#!/usr/bin/python3
""" a function that returns a key with the biggest integer value. """


def best_score(a_dictionary):
    if (a_dictionary) is None:
        return None

    max_key = None
    max_value = float('-inf')  # Set initial max_value to negative infinity

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
