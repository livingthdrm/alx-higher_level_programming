#!/usr/bin/python3
""" a function that replaces an element in a list at a specific
position without modifying the original list (like in C) """


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > (len(my_list) - 1):
        return my_list
    my_l = []
    for index, item in enumerate(my_list):
        if index != idx:
            my_l.append(item)
        else:
            my_l.append(element)

    return my_l
