#!/usr/bin/python3
"""module rectangle.
Creates a class rectangle that inherits from Base
"""


from models.base import Base
import json

class Rectangle(Base):
    """Class rectangle 
    inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a rectangle instance
        Args:
            width: the width
            height: the height
            x: x value
            y: y value
            id: id value
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""

        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute"""

        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute"""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute"""

        return self.__y

    @width.setter
    def width(self, value):
        """sets the width to value"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height to a value"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("Height must be greater than 0")
        self.__height = 0

    @x.setter
    def x(self, value):
        """sets x to a value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be greater than 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y to avalue"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be greater than 0")
        self.__y = value
        
    def display(self):
        """Displays a Reactangle to stdout"""
        
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()
            
     def __str__(self):
        """Returns a string representation of a Rectangle instance."""

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

        

