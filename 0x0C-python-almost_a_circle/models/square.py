#!/usr/bin/python3
"""module models/square.py
defines a class square that inherits from Rectangle
"""


from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square inheriting from Rectangle
    public instance methods:
        area()
        to_dictionary()
        update()
        display()
    """
