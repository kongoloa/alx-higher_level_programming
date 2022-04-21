#!/usr/bin/python3
def no_c(my_string):
        mytable = my_string.maketrans("", "", "cC")
        return my_string.translate(mytable)
