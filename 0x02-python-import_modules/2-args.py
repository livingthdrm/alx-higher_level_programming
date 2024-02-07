#!/usr/bin/python3
""" a program that prints the number of and the list of its arguments """

if __name__ == '__main__':
    def prog(*argv):
        for item in argv:
            if len(argv) == 1:
                print("0 arguments.")
            elif len(argv) == 2:
                print("1 argument:")
                print("{}: {}".format((item + 1), argv(item + 1)))
            else:
                print("{} argument:".format(len(argv) - 1))
                print("{}: {}".format((item + 1), argv(item + 1)))
