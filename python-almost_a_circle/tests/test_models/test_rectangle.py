#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Basic test for rectangle module"""
    def tearDown(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
    
    def test_valid(self):
        """fuction that test for good assignment of differents value"""
        r1 = Rectangle(10, 2, 34, 121, 45027310974)
        self.assertEqual(r1.id, 45027310974)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 34)
        self.assertEqual(r1.y, 121)
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        
    def test_wrong_values(self):
        """test wrong rectangles"""
        with self.assertRaises(TypeError):
            Rectangle("5", 5)
        with self.assertRaises(TypeError):
            Rectangle(5, "5")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
            Rectangle(1, 2, 3, "4")
            Rectangle(-1, 2)
            Rectangle(1, -2)
    
    def test_area(self):
        """test that area exists when
        right arguments provided"""

        r = Rectangle(3, 2).area()
        self.assertEqual(r, 6)

if __name__ == "__main__":
    unittest.main()
    



