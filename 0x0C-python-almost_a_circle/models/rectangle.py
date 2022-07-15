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

    def area(self):
        """Calculates area of a rectangle object
        Returns:
            area
        """
        return self.__width * self.__height
        
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
    
    def update(self, *args, **kwargs):
        """Updates attributes of an instance.
        Args:
            - id attribute
            - width attribute
            - height attribute
            - x attribute
            - y attribute
        """
        
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
