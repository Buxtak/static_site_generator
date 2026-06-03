import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_n_eq_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC, "boot.dev")
        node2 = TextNode("This is a text node", TextType.IMAGE, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_n_eq_link(self):
        node = TextNode("this is text", TextType.CODE, None)
        node2 = TextNode("this is text", TextType.CODE, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_n_eq_test(self):
        node = TextNode("this is text", TextType.CODE, "boot.dev")
        node2 = TextNode("this should be text", TextType.CODE, "boot.dev")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
