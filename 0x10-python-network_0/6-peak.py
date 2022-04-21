#!/usr/bin/python3
"""
 a function that finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """ finds peak """
    if list_of_integers == []:
        return None

    l = len(list_of_integers)
    if l == 1:
        return list_of_integers[0]
    elif l == 2:
        return max(list_of_integers)

    m = int(l / 2)
    peak = list_of_integers[m]
    if peak > list_of_integers[m - 1] and peak > list_of_integers[m + 1]:
        return peak
    elif peak < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m + 1:])
