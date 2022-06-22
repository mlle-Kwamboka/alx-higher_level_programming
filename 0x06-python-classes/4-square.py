#!/usr/bin/python3
"""Class square defined"""


class Square:
    """A new square"""

    def __init__(self, size=0):
        """Initializing size of the square"""

        self.__size = size

    @property
    def size(self):
        """retrieve current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size to a value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return current area of square"""
        
        return self.__size ** 2
    

