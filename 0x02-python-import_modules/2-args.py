#!/usr/bin/python3
""" a program that prints the number of and the list of its arguments """

import sys


def prog(*argv):
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1):
        print("1 argument:")
        print("1: {}".format(argv(0)))
    else:
        print("{} argument:".format(len(argv)))
        
        for i, item in enumerate(argv, start = 1):
            print("{}: {}".format(i, item))

if __name == "__main__":
    prog(*sys.argv[1:])
