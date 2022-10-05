#!/usr/bin/python3
"""unittests stuff to test the stuff
I'm really understanin nothin a t lal
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class for testing Base class"""

    def test_id(self):
        """Test that ID associated exists and match
        with new instances created"""
        b1 = Base()
        b2 = Base(523)
        b3 = Base(62)
        b4 = Base(None)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 523)
        self.assertEqual(b3.id, 62)
        self.assertEqual(b4.id, 2)
        self.assertEqual(b5.id, 3)

    def test_ty_inst(self):
        """test for type and instance"""
        bibi = Base()
        self.assertEqual(type(bibi), Base)
        self.assertTrue(isinstance(bibi, Base))

    def json_(self):
        """test that to_json_string empty exists"""
        bjson = Base.to_json_string([])
        self.assertEqual(bjson, '[]')
