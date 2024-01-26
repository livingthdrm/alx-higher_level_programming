#!/usr/bin/python3
for number in range(0, 100):
    if number == 100 - 1:
        print("{:d}".format(number))
    else:
        print("{:02d}".format(number), end=", ")
