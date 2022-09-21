#!/usr/bin/python3
"""Module checker testeur"""
import unittest
from circles import circle_area
from matrixh import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        """test area when radius >= 0"""
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.5), pi * 2.5**2)

    def test_values(self):
        """Make sure errors are raised when necessary"""
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        """MAke sure type error is raised when necessary"""
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, "chong long!")
        self.assertRaises(TypeError, circle_area, False)
