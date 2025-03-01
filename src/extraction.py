import re

def extract_markdown_images(text):
    image_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_text

def extract_markdown_links(text):
    link_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_text