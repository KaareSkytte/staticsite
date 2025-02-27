from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic_text_"
    CODE = "`Code`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return False
    
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception
        
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
        
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
        
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
        
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
        
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})