#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for letter in str:
        if n < 0 or n > len(str):
            return str
        elif letter != str[n]:
            str1 += "{}".format(letter)
    return str1
