#!/usr/bin/python3
"""unittests stuff to test the stuff
I'm really understanin nothin a t lal
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class for testing Base class"""

    def setUp(self):
        """init our class"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test that ID associated exists and match
        with new instances created"""
        b1 = Base()
        b2 = Base(523)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 523)

    def test_ty_inst(self):
        """test for type and instance"""
        bibi = Base()
        self.assertEqual(type(bibi), Base)
        self.assertTrue(isinstance(bibi, Base))
