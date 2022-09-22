#!/usr/bin/python3
"""Module Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_notinteger(self):
        self.assertIsInstance(max_integer('B'), int)
