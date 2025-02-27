import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        # Test with no properties
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_single(self):
        # Test with a single property
        node = HTMLNode(props={"class": "button"})
        # What should this assert? Think about spaces and quotes
        self.assertEqual(node.props_to_html(), ' class="button"')
    
    def test_props_to_html_multiple(self):
        # Test with multiple properties
        node = HTMLNode(props={
            "class": "button",
            "id": "submit"
        })
        # What would you expect this to return?
        # Remember order might vary with dictionaries
        self.assertEqual(node.props_to_html(), ' class="button" id="submit"')






class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_with_tag(self):
        # Normal case with tag and value
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        # No tag present
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_with_different_tag(self):
        # Testing another tag
        node = LeafNode("a", "Click me")
        self.assertEqual(node.to_html(), "<a>Click me</a>")

    def test_leaf_to_html_no_value(self):
        # Should raise ValueError if no value is provided
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_leaf_to_html_with_props_ignored(self):
        # If props exist, they should not interfere
        node = LeafNode("span", "Test")
        node.props = {"class": "highlight"}  # Set props manually
        self.assertEqual(node.to_html(), "<span>Test</span>")
        # Ensure props do not influence LeafNode's to_html behavior

if __name__ == "__main__":
    unittest.main()