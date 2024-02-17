#!/usr/bin/python3
""" a function that replaces an element of a list
at a specific position (like in C) """


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > (len(my_list) - 1):
        return my_list
    for index, item in enumerate(my_list):
        if index == idx:
            my_list[index] = element
            return my_list