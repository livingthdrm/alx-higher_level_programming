#!/usr/bin/python3
""" a function that adds 2 tuples """


def add_tuple(tuple_a=(), tuple_b=()):
    ptuple_a = tuple_a + (0, 0)
    ptuple_b = tuple_b + (0, 0)
    return (ptuple_a[0] + ptuple_b[0], ptuple_a[1] + ptuple_b[1])




