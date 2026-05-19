from textnode import TextNode, TextType
from extractmarkdownimages import split_nodes_image, split_nodes_link
from splitnodesdelimiter import split_nodes_delimiter

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    delim, text_type = "**", TextType.BOLD 
    nodes = split_nodes_delimiter(nodes, delim, text_type)
    delim, text_type = "_", TextType.ITALIC
    nodes = split_nodes_delimiter(nodes, delim, text_type)
    delim, text_type = "`", TextType.CODE 
    nodes = split_nodes_delimiter(nodes, delim, text_type)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes