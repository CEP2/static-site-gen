from markdowntoblocks import markdown_to_blocks, block_to_block_type
from blocktype import BlockType as BT
from htmlnode import HTMLNode
from parentnode import ParentNode
from texttotextnodes import text_to_textnodes
from textnode import text_node_to_html_node
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    # get blocks
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(create_html_node_from_block(block))
    return ParentNode("div",children)
        

def create_html_node_from_block(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BT.PARAGRAPH:
            return create_paragraph_node(block)
        case BT.HEADING:
            return create_heading_node(block)
        case BT.CODE:
            return create_code_node(block)
        case BT.QUOTE:
            return create_quote_node(block)
        case BT.UNORDERED_LIST:
            return create_unordered_list_node(block)
        case BT.ORDERED_LIST:
            return create_ordered_list_node(block)
        case _:
            raise ValueError("undetected block value")

def create_paragraph_node(block):
    tag = "p"
    paragraph_text = block.replace('\n', '')
    children = text_to_children(paragraph_text)
    return ParentNode(tag,children)

def create_heading_node(block):
    tag = "h" + str(len(block.split(maxsplit=1)[0]))
    text = block.split(" ", maxsplit=1)[1]
    return ParentNode(tag, text_to_children(text))

def create_code_node(block):
    children = [LeafNode("code",block.strip("```"))]
    return ParentNode("pre",children)

def create_quote_node(block):
    tag = "blockquote"
    new_lines = []
    for line in block.split('\n'):
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode(tag,children)
        
def create_unordered_list_node(block):
    tag = "ul"
    lines = block.split('\n')
    children = []
    for line in lines:
        if not line.startswith('- '):
            raise ValueError("invalid unordered list block.")
        children.append(ParentNode("li",text_to_children(line[2:].strip())))
    return ParentNode(tag, children)

def create_ordered_list_node(block):
    tag = "ol"
    index = 1
    lines = block.split('\n')
    children = []
    for line in lines:
        list_num = str(index) + ". "
        if not line.startswith(list_num):
            raise ValueError("invalid ordered list block")
        text = line[2:].strip()
        children.append(ParentNode("li",text_to_children(text)))
        index += 1
    return ParentNode(tag,children)

#helper
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes