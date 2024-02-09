#!/usr/bin/python3

"""a program that imports all functions from the file
calculator_1.py and handles basic operations"""

import sys
from calculator_1 import add, sub, mul, div


def calc(*argv):
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    if argv[1] != '+' or argv[1] != '-' or argv[1] != '*' or argv[1] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    else:
        for item in enumerate(argv, start=1):
            if item[2] == '+':
                result = add(int(item[1]), int(item[3]))
                print("{} + {} = {}".format(item[1], item[3], result))
            elif item[2] == '-':
                result = sub(int(item[1]), int(item[3]))
                print("{} - {} = {}".format(item[1], item[3], result))
            elif item[2] == '*':
                result = mul(int(item[1]), int(item[3]))
                print("{} * {} = {}".format(item[1], item[3], result))
            elif item[2] == '/':
                result = div(int(item[1]), int(item[3]))
                print("{} / {} = {}".format(item[1], item[3], result))


if __name__ == "__main__":
    calc(*sys.argv[1:])
