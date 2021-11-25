#!/usr/bin/python3
def multiply_by_2(dict):
    new_dict = {}
    for x in dict:
        new_dict[x] = dict[x] * 2
    return new_dict
