#!/usr/bin/python3
""" a function that returns the weighted
average of all integers tuple (<score>, <weight>) """


def weight_average(my_list=[]):
    new_dict = dict(my_list)

    first, second = 0, 0

    for score, weight in new_dict.items():
        first += (score * weight)
        second += weight

    return first / second
