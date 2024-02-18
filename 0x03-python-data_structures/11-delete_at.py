#!/usr/bin/python3
""" a function that deletes the item at a specific position in a list """


def delete_at(my_list=[], idx=0):
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    else:
        for index, item in enumerate(my_list):
            if index == idx:
                del my_list[index]
    return my_list
