#!/usr/bin/python3
""" a function that removes all characters c and C from a string """


def no_c(my_string):
    my_str = " "
    for item in my_string:
        if (item != 'c') and (item != 'C'):
            my_str += item

    return my_str
