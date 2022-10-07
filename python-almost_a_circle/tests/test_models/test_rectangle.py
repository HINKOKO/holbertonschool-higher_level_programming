#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

Base._Base__nb_objects = 0

class TestBase(unittest.TestCase):
    """Basic test for rectangle module"""
    
    def test_various_instances(self):
        """Tests with 2, 3, 4 regular args passed
        Then with non valid type or negative integers"""

        r1 = Rectangle(4, 5)
        r2 = Rectangle(5, 6, 7)
        with self.assertRaises(TypeError):
            r3 = Rectangle("5", 6)
            r4 = Rectangle(6, "8")
            r5 = Rectangle(6, 7, "1")
            r6 = Rectangle(6, 5, 8, "9")
            r7 = Rectangle(-5, 5)
            r8 = Rectangle(0, 8)
        self.assertTrue(isinstance(r1, Rectangle), True)
        self.assertTrue(isinstance(r2, Rectangle), True)

    def test_area(self):
        """test that area exists when
        right arguments provided"""

        r = Rectangle(3, 2).area()
        self.assertEqual(r, 6)

    



