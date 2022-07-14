#!/usr/bin/python3
"""unittest Sqaure
test cases for Square numbered accordingly
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test class for the square class"""

    def setUp(self):
        Base._Base__nb_objects = 0


