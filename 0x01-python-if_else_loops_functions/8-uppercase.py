#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            return ord(character) - 32
            print("{}".format(character), end="")
        else:
            print("{}".format(character), end="")
