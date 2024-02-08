#!/usr/bin/python3
""" a program that prints the result of the addition of all arguments """

import sys


def mazematics(*argv):
    result = 0
    for i, item in enumerate(argv, start=1):
        result += int(item)
    print("{}".format(result))


if __name__ == "__main__":
    mazematics(*sys.argv[1:])
