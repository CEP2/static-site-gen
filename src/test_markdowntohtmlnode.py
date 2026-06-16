import unittest
from markdowntohtmlnode import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_heading(self):
        md = "# Hello **world**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Hello <b>world</b></h1></div>")

    def test_unordered_list(self):
        md = "- Item one\n- Item two with `code`"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item one</li><li>Item two with <code>code</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = "1. First item\n2. Second item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li></ol></div>",
        )
    
    def test_quote(self):
        md = "> This is a quote\n> with _italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <i>italic</i> text</blockquote></div>",
        )
    def test_paragraph(self):
        md = """
This is **bolded** paragraph 
text in a p 
tag here
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_code(self):
        md = """```This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )