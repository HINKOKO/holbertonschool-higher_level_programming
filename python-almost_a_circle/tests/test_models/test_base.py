#!/usr/bin/python3
"""unittests stuff to test the stuff
I'm really understanin nothin a t lal
"""
import unittest
import pycodestyle
from models import base
from models import rectangle


class TestStyleFormat(unittest.TestCase):
    """check for pycodestyle"""

    def test_style_conformance(self):
        """Test that we match pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(
            ['models/base.py', 'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings)")

    def TestBase(self):
        """Test that ID associated exists and match"""
        self.assertEqual(Base(12), 12)
        self.asserEqual(Base(5623), 5623)


if __name__ == '__main__':
    unittest.main()
