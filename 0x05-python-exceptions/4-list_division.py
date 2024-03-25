#!/usr/bin/python3
""" a function that divides element by element 2 lists. """


def list_division(my_list_1, my_list_2, list_length):
    try:
        my_list = []
        result = 0
        for item1, item2 in my_list_1, my_list_2:
            result = item1 / item2
            my_list.append(result)
        return my_list
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return my_list
