#!/usr/bin/python3
""" a function that finds the biggest integer of a list """


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for index, item in enumerate(my_list):
            if my_list[index] > my_list[index - 1]:
                return item
