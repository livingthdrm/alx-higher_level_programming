#!/usr/bin/python3
def uppercase(str):
    for character in str:
        str1 = []
        if ord(character) >= 97 and ord(character) <= 122:
            str1.append(chr(ord(character) - 32))
            #print("{}".format(chr(ord(character) - 32)), end="")
        else:
            #print("{}".format(character))
            str1.append(character)
    print("{}".format(str1))
