from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Append non-text nodes as-is
            new_nodes.append(node)
            continue
        
        # Split text nodes by delimiter
        word_list = node.text.split(delimiter)
        
        # Check for unmatched delimiters: valid markdown should alternate, so word_list must have an even length
        if len(word_list) % 2 == 0:
            raise Exception(f"Unmatched delimiter found in text: {node.text}")
        
        else:
            for index, word in enumerate(word_list):
                if index % 2 == 0:
                    # Even-indexed parts are plain TextType.TEXT
                    new_nodes.append(TextNode(word, TextType.TEXT))
                else:
                    # Odd-indexed parts are delimited text with the specified type
                    new_nodes.append(TextNode(word, text_type))

    return new_nodes