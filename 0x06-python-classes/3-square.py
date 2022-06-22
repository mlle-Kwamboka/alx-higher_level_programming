#!/usr/bin/python3
"""Class square defined"""


class Square:
    """A new square"""

    def __init__(self, size=0):
        """initializing instance size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        sel.__size = size

    def area(self):
        """returns current area of a square"""
        return self.__size ** 2

