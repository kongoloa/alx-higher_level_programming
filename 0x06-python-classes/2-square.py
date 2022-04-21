#!/usr/bin/python3
"""defines a class Square"""


class Square():
    """Square class with private instance attribute size"""

    def __init__(self, size=0):
        """ Instantiate a 'Square'"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
