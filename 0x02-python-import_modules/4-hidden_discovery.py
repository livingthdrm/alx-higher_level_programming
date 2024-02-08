#!/usr/bin/python3

""" a program that prints all the names defined by the compiled
module hidden_4.pyc """

if __name__ == "__main__":
    import hidden_4

    if (hidden_4.__name__ != "__main__"):
        print("{}".format(hidden_4.__name__))
