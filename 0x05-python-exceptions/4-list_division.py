#!/usr/bin/python3
""" a function that divides element by element 2 lists. """


def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for x, y in zip(my_list_1, my_list_2):
        try:
            my_list.append(x / y)
        except ZeroDivisionError:
            my_list.append(0)
            print("division by 0")
        except TypeError:
            my_list.append(0)
            print("wrong type")
        except IndexError:
            my_list.append(0)
            print("out of range")
        finally:
            pass
    return my_list
