import unittest

from textnode import TextNode, TextType
from markdown_parser import split_nodes_delimiter

class TestMarkdownParser(unittest.TestCase):
    def testSplitCode(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

    def testDelimAtEnd(self):
        node = TextNode("This has a **bold** at the **end**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[3].text, "end")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)


if __name__ == "__main__":
    unittest.main()