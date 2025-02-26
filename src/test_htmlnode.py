import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()