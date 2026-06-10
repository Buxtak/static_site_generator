import unittest

from gen_content import extract_title


class TitleTest(unittest.TestCase):
    def test_with_title_single_line(self):
        markdown = "# This is the title"
        result = "This is the title"
        self.assertEqual(extract_title(markdown), result)

    def test_with_title_multiline(self):
        markdown = """# This is the title\n
            this is another line\n
            this is the last line """
        result = "This is the title"
        self.assertEqual(extract_title(markdown), result)

    def test_without_title(self):
        markdown = "there is no title"
        with self.assertRaises(Exception):
            extract_title(markdown)
