#!/usr/bin/python3
""" a function that returns a tuple with the length of
a string and its first character """


def multiple_returns(sentence):
    for item in sentence:
        if (len(sentence) < 1):
            return (len(sentence), None)
        return (len(sentence), sentence[0],)
