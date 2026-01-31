import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init_tag(self):
        node = HTMLNode("p")
        self.assertEqual(node.tag, "p")

    def test_init_value(self):
        node = HTMLNode("p", "value")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "value")

    def test_props_to_html(self):
        props = {}
        props["key"] = "value"

        expected_props_string = ' key="value"'
        node = HTMLNode("p", "value", props=props)

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "value")
        self.assertEqual(node.props_to_html(), expected_props_string)
