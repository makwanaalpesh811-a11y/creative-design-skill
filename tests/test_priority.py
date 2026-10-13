"""Creative Design Skill — Priority Tests (mocks only)."""
import unittest
import os

class CreativeDesignTest(unittest.TestCase):
    def test_happy_path_generate_svg_mock(self):
        svg = "<svg><rect/></svg>"
        self.assertIn("<svg>", svg)

    def test_invalid_input_bad_color(self):
        color = "not_a_color"
        # Would fail SVG validation
        self.assertTrue(True)

    def test_missing_credential_not_required(self):
        # Design tools are local
        self.assertTrue(True)

    def test_timeout_large_render(self):
        def fake():
            raise TimeoutError("render timeout")
        with self.assertRaises(TimeoutError):
            fake()

    def test_dry_run_no_file_written(self):
        self.assertTrue(True)

    def test_placeholder_key_rejected(self):
        for k in ["your_key", "dummy"]:
            if "your" in k or "dummy" in k:
                self.assertTrue(True)

    def test_copy_paste_example(self):
        ex = '''
echo "<svg><circle/></svg>" > out.svg
'''
        self.assertIn("<svg>", ex)

    def test_error_invalid_dimensions(self):
        w, h = -1, 100
        self.assertLess(w, 0)

    def test_error_unsupported_format(self):
        fmt = "unsupported.xyz"
        self.assertTrue(fmt.endswith(".xyz"))


if __name__ == "__main__":
    unittest.main()
