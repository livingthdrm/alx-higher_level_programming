#!/usr/bin/python3
"""This program imports a module then utilizes it"""
if __name__ = "__main__":
    from add_0 import add
        a = 1
        b = 2
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
