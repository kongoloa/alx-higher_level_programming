#!/usr/bin/python3
"""Defines a class Square"""


class Square():
    """Square class with private instance attribute size"""

    def __init__(self, size=0):
        """initializes the square"""
        self.size = size

    @property
    def size(self):
        """Get the size of a square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute the area of a Square"""
        return self.size ** 2

    def my_print(self):
        """Print a visual representation of a square"""
        print('\n'.join(['#' * self.size] * self.size))
