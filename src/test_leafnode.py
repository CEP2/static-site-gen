import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!").to_html()
        self.assertEqual(node, "<p>Hello, world!</p>") 

        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        correct = '<a href="https://www.google.com">Click me!</a>'       
        self.assertEqual(node, correct)
        

if __name__ == "__main__":
    unittest.main()