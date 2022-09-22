#!/usr/bin/python3
"""Module Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_notinteger(self):
        """test what happens when not integers are passed"""
        self.assertNotIsInstance(max_integer('B'), int)

    def test_max_at_end(self):
        """test when max integer at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """test when max integer at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
