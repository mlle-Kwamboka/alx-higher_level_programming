#!/usr/bin/python3
"""Class Square defined"""

class Square:
    """A new square created"""

    def __init__(self, size=0):
        """object size initialized"""

        self.__size = size

    @property
    def size(self):
        """current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size to value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
    """set position to value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or nor isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """return the area of square"""
        return self.__size ** 2

    def my_print(self):
        """print square to stdout using character #"""
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__postion[1]):
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print()


