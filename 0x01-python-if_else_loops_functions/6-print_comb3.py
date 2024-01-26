#!/usr/bin/python3
for number1 in range(0, 10):
    for number2 in range(1, 10):
        if number1 != number2 and number1 < number2:
            print("{number1}{number2}".format(number1, number2))
