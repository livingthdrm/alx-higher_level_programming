#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for letter in str:
        if letter != str[n]:
            str1 += "{}".format(letter)
    return str1
