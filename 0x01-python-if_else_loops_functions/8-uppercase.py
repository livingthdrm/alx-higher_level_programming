#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            print("{}".format(chr(ord(character) - 32))) 
        else:
            print("{}".format(character))
        
