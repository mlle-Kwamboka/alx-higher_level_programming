#!/usr/bin/python3
"""module base
Defines a class base for all other classes in this project
"""

import os
import Json
import csv


class Base:
    """Class Base created with private attribute __nb_objects = 0

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of class base instance
        Args:
            id: The id of class
        """
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = __nb_objects
        


