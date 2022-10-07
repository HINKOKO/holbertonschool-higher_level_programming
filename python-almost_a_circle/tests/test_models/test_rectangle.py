#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


def setUpModule():
	print("setup module or not")
def tearDownModule():
	print("module tornDown")

class TestBase(unittest.TestCase):
	"""Basic test for rectangle module"""
	
	def test_various_instances(self):
		"""Tests with 2, 3, 4 regular args passed
		Then with non valid type or negative integers"""
		r1 = Rectangle(10, 1)
		r2 = Rectangle(10, 2, 0, 0, 12)
		self.assertEqual(r1.id, 3)
		self.assertEqual(r2.id, 12)
		self.assertEqual(r2._Base__nb_objects, 3)

		with self.assertRaises(TypeError):
			r3 = Rectangle("5", 6)
			r4 = Rectangle(6, "8")
			r5 = Rectangle(6, 7, "1")
			r6 = Rectangle(6, 5, 8, "9")
			r7 = Rectangle(-5, 5)
			r8 = Rectangle(0, 8)

	def test_area(self):
		"""test that area exists when
		right arguments provided"""

		r = Rectangle(3, 2).area()
		self.assertEqual(r, 6)
	



