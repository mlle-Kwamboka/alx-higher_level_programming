#!/usr/bin/python3
"""Module 2-rectangle
Defines a Rectangle class"""

class Rectangle:
    """A rectangle"""
    def __init__(self, width=0, height=0):

        """Initializing a rectangle object
        Args:
        width: A positive integer, the width of the rectangle
        height: The height, always a positive integer
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width to value
        Args:
        Value: Positive integer representing width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height to a value
        Args: 
        value: positive integer representing height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)


