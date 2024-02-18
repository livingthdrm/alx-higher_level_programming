#!/usr/bin/python3
""" a function that finds all multiples of 2 in a list. """


def divisible_by_2(my_list=[]):
    my_list2 = []

    for item in my_list:
        if item % 2 == 0:
            my_list2.append(True)
        else:
            my_list2.append(False)
    return my_list2
