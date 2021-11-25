#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_del = []
    for x in a_dictionary:
        if a_dictionary[x] == value:
            keys_to_del.append(x)
    for key in keys_to_del:
        del a_dictionary[x]
    return a_dictionary
