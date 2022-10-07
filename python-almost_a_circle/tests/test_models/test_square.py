#!/usr/bin/python3
"""
This is the "test_square" module
Thes test_square module supplies a class to test class Square
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os.path import exists
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """
    test classe square
    """

    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    # Test the correct values

    def test_correct_values(self):
        r1 = Square(2, 4, 6)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 4, 6, 50)
        self.assertEqual(r2.size, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 6)
        self.assertEqual(r2.id, 50)

        r3 = Square(2)
        self.assertEqual(r3.size, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 2)

    def test_priority_width_height(self):
        with self.assertRaises(ValueError):
            Square(-2, -6, -4)
        with self.assertRaises(TypeError):
            Square("str", "str", 3, None)
        with self.assertRaises(TypeError):
            Square("str", -2, 3, None)
        with self.assertRaises(ValueError):
            Square(-1, -2, 3, None)
        with self.assertRaises(ValueError):
            Square(-1, "str", 3, None)

    # Test for valueError

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-5, 10, 8)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0, 10, 8)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(5, -10, 8)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(5, 10, -8)

    # Test for wrongType

    def test_x_wrongType(self):
        with self.assertRaises(TypeError):
            Square(5, "10", 8)

    def test_y_wrongType(self):
        with self.assertRaises(TypeError):
            Square(5, 10, "8")

    def test_str(self):
        r1 = Square(10, 10, 0)
        r2 = Square(10)
        r3 = Square(10, 10, 10, 50)
        self.assertEqual(r1.__str__(), "[Square] (1) 10/0 - 10")
