#!/usr/bin/python3
""" a function that prints all integers of a list, in reverse order """


def print_reversed_list_integer(my_list=[]):
    my_l = my_list[::-1]
    for item in my_l:
        print("{:d}".format(item))
