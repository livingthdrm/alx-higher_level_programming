#!/usr/bin/python3
"""a function that raises a type exception"""


def raise_exception():
    try:
        raise TypeError
    finally:
        pass
