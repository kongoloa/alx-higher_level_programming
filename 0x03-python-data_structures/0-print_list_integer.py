#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in my_list:
        if isinstance(x, int):
            print("{:d}".format(x))
