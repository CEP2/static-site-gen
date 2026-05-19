import re
from textnode import TextNode, TextType

LINK_EXPR = r"\[(.*?)\]\((.*?)\)"
IMG_EXPR = '!'+LINK_EXPR

'''
In: Raw .md text
out: list of tuples - alt text and url of any markdown images.

Looking For: ![alt-text](Image URL)
'''
def extract_markdown_images(text):

    expr = r"!\[(.*?)\]\((.*?)\)"
    results = re.findall(expr, text)

    return results

'''
In: Raw .md text
out: list of tuples - alt text and url of any markdown images.

Looking For: ![text](url)
'''
def extract_markdown_links(text):

    results = re.findall(LINK_EXPR, text)

    return results

def split_nodes_image(old_nodes):
    text_type = TextType.IMAGE
    new_nodes = []
    for old in old_nodes:
        new_subnodes = []
        if not isinstance(old, TextNode):
            raise ValueError("not a TextNode node.")
        if old.text_type != TextType.TEXT:
            new_subnodes.append(old)
        else:
            txt = old.text
            matches = re.findall(IMG_EXPR,txt)
            txt_split = []
            # loop through each match...
            for m in matches:
                # fmt delim; m[0] = text, m[1] = link
                m_text = m[0]
                m_link = m[1]
                delim = f"![{m_text}]({m_link})"
                # split based on match...
                txt_split = txt.split(sep=delim, maxsplit=1)
                cur_text = txt_split[0]
                rest_text = txt_split[1]
                # [0] is text to be processed...
                if cur_text != '':
                    new_subnodes.append(TextNode(cur_text,TextType.TEXT))                
                # process m (current match) into text_type TextNode
                new_subnodes.append(TextNode(m_text, text_type, url=m_link))
                # make [1] new text to be split.
                txt = txt_split[1]
            #process final [1], remainder of text. 
            if txt != '':
                new_subnodes.append(TextNode(txt, TextType.TEXT))
        new_nodes.extend(new_subnodes)            
    return new_nodes

def split_nodes_link(old_nodes):
    text_type = TextType.LINK
    new_nodes = []
    for old in old_nodes:
        new_subnodes = []
        if not isinstance(old, TextNode):
            raise ValueError("not a TextNode node.")
        if old.text_type != TextType.TEXT:
            new_subnodes.append(old)
        else:
            txt = old.text
            matches = re.findall(LINK_EXPR,txt)
            txt_split = []
            # loop through each match...
            for m in matches:
                # fmt delim; m[0] = text, m[1] = link
                m_text = m[0]
                m_link = m[1]
                delim = f"[{m_text}]({m_link})"
                # split based on match...
                txt_split = txt.split(sep=delim, maxsplit=1)
                cur_text = txt_split[0]
                rest_text = txt_split[1]
                # [0] is text to be processed...
                if cur_text != '':
                    new_subnodes.append(TextNode(cur_text,TextType.TEXT))                
                # process m (current match) into text_type TextNode
                new_subnodes.append(TextNode(m_text, text_type, url=m_link))
                # make [1] new text to be split.
                txt = txt_split[1]
            #process final [1], remainder of text. 
            if txt != '':
                new_subnodes.append(TextNode(txt, TextType.TEXT))
        new_nodes.extend(new_subnodes)            
    return new_nodes
