#!/usr/bin/python3

""" a program that prints all the names defined by the compiled
module hidden_4.pyc """

if __name__ == "__main__":
    from hidden_4 import *

    if hidden_4.__name__ == "hidden_4":
        print("{}".format(dir()))
