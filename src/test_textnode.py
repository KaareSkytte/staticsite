import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Identical nodes are Eequal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        # Nodes with different text content are not equal
        node3 = TextNode("This is a text node3", TextType.BOLD)
        self.assertNotEqual(node, node3)

        # A node with explicit None URL equals one without URL specified
        node4 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node4)

        # Nodes with different text types are not equal
        node5 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node5)

        # Nodes with different URLs are not equal
        node6 = TextNode("This is a text node", TextType.BOLD, "randomurl")
        self.assertNotEqual(node, node6)

        # A node is not equal to a completely different type (string)
        random_string = "This is a test"
        self.assertNotEqual(node, random_string)

if __name__ == "__main__":
    unittest.main()