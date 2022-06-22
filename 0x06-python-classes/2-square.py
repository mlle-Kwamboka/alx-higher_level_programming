#!/usr/bin/python3
"""Class square defined"""


class Square:
    """A new square"""
    
    def __init__(self, size=0):
        """Initialize a new square with args size of type int"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError(size must be >= 0)
        self.__size = size
