#!/usr/bin/python3
"""unittest base.
test cases for base class
Each test has a number corresponding to task: eg test_1_0 corresponds to task
number 1
"""

import unittest
import os
from models.base import Base

class TestBase(unittest.TestCase):
    """test class for Base class"""

    def setUp(self):
         Base.Base.__nb_objects = 0

    def test_1_0(self):
        """Creates new Instances: check for id"""
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base(4)
        self.assertEqual(b4.id, 4)

    def test_1_1(self):
        """tests for type and Instance"""
        b4 = Base()
        self.assertEqual(type(b4), Base)
        self.assertTrue(isinstance(b4, Base))