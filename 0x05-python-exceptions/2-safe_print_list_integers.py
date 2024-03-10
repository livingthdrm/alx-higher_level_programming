#!/usr/bin/python3
""" a function that prints the
first x elements of a list and only integers."""


def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for item in my_list[:x]:
            if type(item) != int:
                continue
            else:
                print("{:d}".format(item), end="")
                count += 1
        print()
        return count
    except IndexError:
        print("list index out of range")
