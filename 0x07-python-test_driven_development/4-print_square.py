#!/usr/bin/python
"""
Module print_square
prints a square

"""
def print_square(size):
    """Prints a square to stdout using the character #"""
    if type(size) is not int:
        raise TypeError("Size must be an integer")

    if size < 0
        raise TypeError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
            print()
