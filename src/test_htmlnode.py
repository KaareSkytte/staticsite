import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        node = LeafNode("span", "Test", {"class": "highlight"})
        node.props = {"class": "highlight"}  # Set props manually
        self.assertEqual(node.to_html(), '<span class="highlight">Test</span>')
        # Ensure props do not influence LeafNode's to_html behavior



class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("i", "italic text")
        child2 = LeafNode(None, "normal text")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><i>italic text</i>normal text</div>",
        )

    def test_to_html_with_deep_nesting(self):
        great_grandchild = LeafNode(None, "great grandchild")
        grandchild = ParentNode("b", [great_grandchild])
        child = ParentNode("span", [grandchild])
        parent_node = ParentNode("div", [child])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>great grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()