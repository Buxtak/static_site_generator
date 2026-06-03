import unittest

from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestBlockNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_block(self):
        md = "## heading 2"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.HEADING)

    def test_code_block(self):
        md = "```\n line of code \n```"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.CODE)

    def test_quote_block(self):
        md = "> quote 1\n> quote 2\n> quote 3"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.QUOTE)

    def test_unordered_block(self):
        md = "- list element 1\n- list element 2\n- list element 3"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.UNORDERED_LIST)

    def test_ordered_block(self):
        md = "1. numbered element 1\n2. numbered element 2\n3. numbered element 3"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        md = "1. numbered element 1\nparagraph continuation just because"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.PARAGRAPH)
