class TestStyleFormat(unittest.TestCase):
    """check for pycodestyle"""

    def test_style_conformance(self):
        """Test that we match pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(
            ['models/base.py', 'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings)")

    def json_string(self):
        """test that empty json string exists"""
        bjson = Base.to_json_string([])
        self.assertEqual(bjson, '[]')
