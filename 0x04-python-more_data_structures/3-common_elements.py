#!/usr/bin/python3
""" a function that returns a set of common elements in two sets. """


def common_elements(set_1, set_2):
    #common_set = set()
    #for element1 in set_1:
        #for element2 in set_2:
           #if element1 == element2:
                #common_set.add(element1)
    #return common_set
    return set(set_1 & set_2)
