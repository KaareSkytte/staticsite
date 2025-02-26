from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal text"
    BOLD_TEXT = "**Bold text**"
    ITALIC_TEXT = "_Italic_text_"
    CODE_TEXT = "`Code`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"