from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"



def markdown_to_blocks(markdown):
    new_paragraphs = []
    
    # Split into paragraphs by double newlines
    markdown_paragraphs = markdown.split("\n\n")
    
    for paragraph in markdown_paragraphs:
        # First strip the entire paragraph to handle leading/trailing newlines
        paragraph = paragraph.strip()
        
        # Skip empty paragraphs after stripping
        if not paragraph:
            continue
        
        # Split paragraph into lines
        lines = paragraph.split("\n")
        
        # Strip each line
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.strip())
        
        # Join lines back into a paragraph
        clean_paragraph = "\n".join(stripped_lines)
        
        # Only add non-empty paragraphs
        if len(clean_paragraph) != 0:
            new_paragraphs.append(clean_paragraph)
    
    return new_paragraphs


def block_to_block_type(block):
    # Heading Check: Starts with 1-6 '#' followed by a space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    # Code Block: Starts and ends with three backticks (```).
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Split the block by lines for list and quote checks
    lines = block.split("\n")
    
    # Quote Block: All lines must start with '>'
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Unordered List: All lines must start with '- '
    if all(line.startswith("- ") for line in lines):
        return BlockType.ULIST
    
    # Ordered List: All lines must start with incrementing numbers followed by '. '
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.OLIST
    
    # Default to Paragraph Block
    return BlockType.PARAGRAPH