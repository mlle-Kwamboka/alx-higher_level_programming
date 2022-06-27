#!/usr/bin/python3
""" Defining a rectangle"""

class Rectangle:
    
    """represents a new rectangle"""
    def __init__(self, width=0, height=0):
        """initializes a new rectangle
        Args: 
        width (int): the width of the new rectangle
        height (int): the height of the new rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets widtth to a value"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < o:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height to a value"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

   

