

import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from splitnodesdelimiter import split_nodes_delimiter


delim = '`'
test_str = ["This is a `code block`",
            "`code block`",
            "`code block` this can be fun",
            "",
            "`almost code block",
]

class test_split_node_delimiter(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        text_type = TextType.CODE
        delim = '`'
        test_strs = {"This is a `code block`":[
            TextNode("This is a ",TextType.TEXT),
            TextNode("code block", text_type)
            ],
            "`code block`":[
                TextNode("code block",text_type)
            ],
            "`code block` this can be fun":[
                TextNode("code block", text_type),
                TextNode(" this can be fun", TextType.TEXT)
            ],
            "":[],
        }
        for node in test_strs:
            old_node = TextNode(node,TextType.TEXT)
            new_nodes = split_nodes_delimiter([old_node],delim,text_type)
            num_new = len(new_nodes)
            self.assertEqual(num_new, len(test_strs[node]))
            for n in range(num_new):
                #look at each in order...
                expected = test_strs[node][n] 
                result   = new_nodes[n]
                self.assertEqual(expected, result)

    def test_split_nodes_delimiter_error(self):
        text_type = TextType.CODE
        delim = '`'
        test_str = "`almost code block"
        old_node = TextNode(test_str, TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([old_node], delim, text_type)
        
    

        

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "https://www.bing.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()