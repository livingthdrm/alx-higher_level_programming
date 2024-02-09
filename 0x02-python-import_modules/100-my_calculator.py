#!/usr/bin/python3

"""a program that imports all functions from the file
calculator_1.py and handles basic operations"""

import sys
from calculator_1 import add, sub, mul, div


def calc(*argv):
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    operator = argv[1]

    if operator not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1

    a, b = map(int, argv[::2])
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    calc(*sys.argv[1:])
