#!/usr/bin/python3
"""unittest rectangle
test cases for the rectangle class numbered accodingly
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    """Test case for the rectangle class"""

    def set_up(self):
        Base._Base__nb_objects = 0

    def test_2_0(self):
        """Test for rectangle: checking id"""

        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(10, 1, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(5, 2, 0, 1, 9)
        self.assertEqual(r4.id, 9)
        r5 = Rectangle(6, 2, 1, 1, -3)
        self.assertEqual(r5.id, -5)
        r6 = Rectangle(10, 2, 0, 3, 25)
        self.assertEqual(r6.id, 25)


    def test_2_1(self):
        """Test for attribute values"""
        r0 = Rectangle(5, 2)
        self.assertEqual(r0.width, 5)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 0)
        self.assertEqual(r0.y, 0)
        r1 = Rectangle(5, 2, 3, 4, 25)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

