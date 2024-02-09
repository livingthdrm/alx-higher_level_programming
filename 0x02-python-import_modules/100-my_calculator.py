#!/usr/bin/python3

"""a program that imports all functions from the file
calculator_1.py and handles basic operations"""

import sys
from calculator_1 import add, sub, mul, div


def calc(*argv):
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    if (argv[1] != chr(43) or argv[1] != chr(45)
    or argv[1] != chr(42) or argv[1] != chr(47)):
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    else:
        for item in argv:
            if item[1] == chr(43):
                result = add(int(item[0]), int(item[2]))
                print("{} + {} = {}".format(item[0], item[2], result))
            elif item[1] == chr(45):
                result = sub(int(item[0]), int(item[2]))
                print("{} - {} = {}".format(item[0], item[2], result))
            elif item[1] == (42):
                result = mul(int(item[0]), int(item[2]))
                print("{} * {} = {}".format(item[0], item[2], result))
            elif item[1] == (47):
                result = div(int(item[0]), int(item[2]))
                print("{} / {} = {}".format(item[0], item[2], result))


if __name__ == "__main__":
    calc(*sys.argv[1:])
