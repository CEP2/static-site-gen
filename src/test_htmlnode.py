import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        # node = TextNode("This is a text node", TextType.BOLD)
        # node2 = TextNode("This is a text node", TextType.BOLD)
        # self.assertEqual(node, node2)

        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "Link to Google", props=test_props)
        to_html_soln = " href=\"https://www.google.com\" target=\"_blank\""
        to_html = node.props_to_html()
        self.assertEqual(to_html, to_html_soln)

        test_props = {
            "id": "556869",
            "title": "Google Tutorial",
        }
        key_list = list(test_props.keys())
        node = HTMLNode("p", "Let's show how to visit google.com.", props=test_props)
        to_html_soln = f" {key_list[0]}=\"{test_props[key_list[0]]}\" {key_list[1]}=\"{test_props[key_list[1]]}\""
        to_html = node.props_to_html()
        self.assertEqual(to_html, to_html_soln)

        node = HTMLNode("p", "Let's show how to visit google.com.")
        to_html_soln = ""
        to_html = node.props_to_html()
        self.assertEqual(to_html, to_html_soln)        
        

if __name__ == "__main__":
    unittest.main()