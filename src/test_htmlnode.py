import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("h1", "this is header 1")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "this is header 1")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_props(self):
        node = HTMLNode(
            "a",
            "Boot.dev",
            None,
            {
                "href": "https://www.boot.dev",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.boot.dev" target="_blank"'
        )

    def test_repr(self):
        node = HTMLNode("div", "text", None, {"class": "box"})
        self.assertEqual(repr(node), "HTMLNode(div, text, None, {'class': 'box'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_w_props(self):
        node = LeafNode("a", "Boot.dev", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Boot.dev</a>')

    def test_leaf_repr(self):
        node = LeafNode("div", "text", {"class": "box"})
        self.assertEqual(repr(node), "LeafNode(div, text, {'class': 'box'})")


if __name__ == "__main__":
    unittest.main()
