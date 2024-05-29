#!/usr/bin/python3
"""
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Prototype: def text_indentation(text):
"""


def text_indentation(text):
    """
    A function that outputs the string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False
    for words in text:
        if words in ('.', '?', ':'):
            print(words)
            print()
            skip_space = True
        elif words == ' ' and skip_space:
            continue
        else:
            print(words, end="")
            skip_space = False
