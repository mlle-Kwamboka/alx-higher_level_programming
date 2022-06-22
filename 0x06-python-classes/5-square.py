#!/usr/bin/python3
"""Class Square defined"""


class Square:
    """new Square defined"""

    def __init__(self, size=0):
        """initializing instance size"""

        self.__Size = size

    @property
    def size(self):
        """retrieve current size"""
        return self.__size

    @size.setter
    def size(self):
        """set size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current area"""
        return self.__size ** 2

    def my_print(self):
        """prints a square to stdout using character #"""
        if self.__size = 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
    
