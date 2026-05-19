from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        current_node_subnodes = []
        if not isinstance(node, TextNode):
            raise ValueError("not a TextNode node.")
        if node.text_type != TextType.TEXT:
            current_node_subnodes.append(node)
        else:
            text_list = node.text.split(sep=delimiter)
            if len(text_list) % 2 == 0:
                #there should always be an odd # of segments with opening and closing delims.
                raise ValueError(f"delim isn't closed. check {node.text}")
            is_block = False #first block is always outside, even if empty.
            for text in text_list:
                #check for blank
                if text != '':
                    cur_type = text_type if is_block else TextType.TEXT
                    cur_new_node = TextNode(text, cur_type)
                    current_node_subnodes.append(cur_new_node)
                is_block = not is_block
        # if len(current_node_subnodes) != 0:
        new_nodes.extend(current_node_subnodes)

    return new_nodes