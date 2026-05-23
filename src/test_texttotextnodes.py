from extractmarkdownimages import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode
from texttotextnodes import text_to_textnodes
import unittest

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):

        test_string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(test_string)
        # print(new_nodes, sep='\n')
        self.assertListEqual(
            [   
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),   
            ],
            new_nodes,
        )
    
if __name__ == "__main__":
    unittest.main()