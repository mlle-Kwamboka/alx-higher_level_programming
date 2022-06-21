#!/usr/bin/python3
class Square:
    """Definition of a square"""
    def __init__(self, size=0):
        self.__size = size
        try:
            print("square size: {:d}".format(self.__size))
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
p = Square()
p.size
