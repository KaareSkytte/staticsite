import unittest
from textnode import TextType, TextNode
from delimiter import split_nodes_delimiter  # Replace `your_module_name` with the module where your function is defined

class TestSplitNodesDelimiter(unittest.TestCase):

    
    def test_single_delimiter(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        old_nodes = [node]
        
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]
        
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")
    
    
    def test_no_delimiter(self):
        node = TextNode("This is plain text with no delimiters", TextType.TEXT)
        old_nodes = [node]
        
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected = [TextNode("This is plain text with no delimiters", TextType.TEXT)]
        
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    
    def test_unmatched_delimiter_start(self):
        node = TextNode("This is `code without end", TextType.TEXT)
        old_nodes = [node]
        
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        
        self.assertEqual(str(context.exception), 
                         "Unmatched delimiter found in text: This is `code without end")
        
    
    def test_unmatched_delimiter_end(self):
        node = TextNode("Unmatched end delimiter` here", TextType.TEXT)
        old_nodes = [node]
        
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        
        self.assertEqual(str(context.exception), 
                         "Unmatched delimiter found in text: Unmatched end delimiter` here")
        

if __name__ == "__main__":
    unittest.main()