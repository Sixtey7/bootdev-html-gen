import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_init_value(self):
        node = LeafNode("p", "value")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "value")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Hello, world!", {"href": "http://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="http://boot.dev">Hello, world!</a>')