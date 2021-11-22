#!/usr/bin/python3
def element_at(x, y):
    if y < 0:
        return None
    if y > len(x):
        return None
    else:
        return x[y]
