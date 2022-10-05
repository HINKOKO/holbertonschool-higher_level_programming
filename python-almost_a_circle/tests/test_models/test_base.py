#!/usr/bin/python3
"""unittests stuff to test the stuff
I'm really understanding nothing at all
"""
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """class for testing Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test that ID associated exists and match
        with new instances created"""
        b1 = Base()
        b2 = Base(523)
        b3 = Base(62)
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 523)
        self.assertEqual(b3.id, 62)
        self.assertEqual(b4.id, 2)
        self.assertEqual(b5.id, 3)

    def test_type(self):
        """test type and instance"""
        b = Base()
        self.assertTrue(isinstance(b, Base))
        self.assertEqual(type(b), Base)

    def test_json_str_empty(self):
        """test if empty list produce what expected"""
        bjson = Base.to_json_string([])
        self.assertEqual(bjson, '[]')
