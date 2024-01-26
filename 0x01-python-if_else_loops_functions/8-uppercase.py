#!/usr/bin/python3
def uppercase(input_str):
    converted_str = ""
    for character in input_str:
        if ord(character) >= 97 and ord(character) <= 122:
            converted_str += "{}".format(chr(ord(character) - 32))
        else:
            converted_str += "{}".format(character)

    print(converted_str)
