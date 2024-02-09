#!/usr/bin/python3

""" a program that prints all the names defined by the compiled
module hidden_4.pyc """

if __name__ == "__main__":
    import hidden_4

    if hidden_4.__name__ == "hidden_4":
        module_names = [name for name in dir(hidden_4) if not name.startswith('__')]
        print("{}".format(module_names))
