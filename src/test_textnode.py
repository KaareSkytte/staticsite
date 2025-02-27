import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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



class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_text_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")


    def test_text_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        # Assert the HTML node has the expected properties
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "https://www.example.com")

    def test_text_image(self):
        # Create a TextNode with IMAGE type, alt text, and a source URL
        url = "https://www.example.com/image.png"
        alt_text = "An example image"
        node = TextNode(alt_text, TextType.IMAGE, url)
    
        # Convert to HTML node
        html_node = text_node_to_html_node(node)
    
        # Assert the HTML node has the expected properties
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  # Empty string for images
        self.assertEqual(html_node.props["src"], url)
        self.assertEqual(html_node.props["alt"], alt_text)



if __name__ == "__main__":
    unittest.main()