def test_diplay(self):
        """Check display func"""
        r1 = Rectangle(5, 6)
        r2 = Rectangle(8, 7, 3, 2, 4)
        with io.StringIO() as buf, redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 5 + "\n") * 6)
        with io.StringIO() as buf, redirect_stdout(buf):
            r2.display()
            output = buf.getvalue()
            self.assertEqual(
                output, (2 * "\n" + (" " * 3 + "#" * 8 + "\n") * 7))
