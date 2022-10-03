#!/usr/bin/python3
"""unittests stuff to test the stuff
I'm really understanin nothin a t lal
"""
import unittest
import pycodestyle
from models.base import Base


class TestStyleFormat(unittest.TestCase):
    """check for pycodestyle"""

    def test_style_conformance(self):
        """Test that we match pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(
            ['models/base.py', 'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings)")


class TestBase(unittest.TestCase):
    """class for testing Base class"""

    def test_id(self):
        """Test that ID associated exists and match
        with new instances created"""
        b1 = Base()
        b2 = Base(523)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 523)
