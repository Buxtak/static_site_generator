import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is a `code` node", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" node", TextType.TEXT),
            ],
        )

    def test_bold_delimiter(self):
        node = TextNode("This is a **bold** node", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" node", TextType.TEXT),
            ],
        )

    def test_italic_delimiter(self):
        node = TextNode("This is an _italic_ node", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            result,
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" node", TextType.TEXT),
            ],
        )

    def test_multiple_italic_delimiter(self):
        node = TextNode(
            "This is an _italic_ node with an extra _italic_ word", TextType.TEXT
        )
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            result,
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" node with an extra ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_invalid_markdown(self):
        node = TextNode("This is an _italic node", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_not_text(self):
        node = TextNode("This is an _italic_ node", TextType.ITALIC)
        result = split_nodes_delimiter([node], "_", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("This is an _italic_ node", TextType.ITALIC),
            ],
        )
