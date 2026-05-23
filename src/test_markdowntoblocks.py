import unittest
from markdowntoblocks import markdown_to_blocks, block_to_block_type
from blocktype import BlockType

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
    

    def test_block_to_block_type_paragraph(self):
          expected = BlockType.PARAGRAPH
          blocks_to_test = [
                "this is block text for a paragraph",                
          ]
          for block in blocks_to_test:
                actual = block_to_block_type(block)
                self.assertEqual(actual,expected, msg=f"Expected {expected}, got {actual} on {block}")
    
    def test_block_to_block_type_heading(self):
        expected = BlockType.HEADING
        blocks_to_test = [
            "# this is block text for a heading",
            "## this is block text for a heading 2",
            "### this is block text for a heading 3",
            "#### this is block text for a heading 4",
            "##### this is block text for a heading 5",
            "###### this is block text for a heading 6",
        ]
        blocks_to_fail = [
            "!# incorrect character at start",
            "this is block text is a para",
            " ### space at start",
            "####this has no space between hashes and start of words",
            "####### 7, more than max heading",
        ]
        for block in blocks_to_test:
            actual = block_to_block_type(block)
            self.assertEqual(actual,expected, msg=f"Expected {expected}, got {actual} on {block}")

        expected = BlockType.PARAGRAPH
        for block in blocks_to_fail:
            actual = block_to_block_type(block)
            self.assertEqual(actual,expected, msg=f"Expected {expected}, got {actual} on {block}")
     
    def test_block_to_block_type_code(self):
        expected = BlockType.CODE
        blocks_to_test = [
                '''```
this is a code block.
                ```''',
                '''```
this is a code block w/ticks at the end of the line.```''',         
          ]
        for block in blocks_to_test:
            actual = block_to_block_type(block)
            self.assertEqual(actual,expected, msg=f"Expected {expected}, got {actual} on {block}")

        expected = BlockType.PARAGRAPH
        blocks_to_fail = [
            "just a paragraph",
            "``` ticks aren't alone on first line ```",
            "```attached text to front```",
            '''``
            not enough starting ticks
            ```''',
            '''```
            not enough ending ticks
            ``'''

        ]
        for block in blocks_to_fail:
            actual = block_to_block_type(block)
            self.assertEqual(actual,expected, msg=f"Expected {expected}, got {actual} on {block}")

    def test_block_to_block_type_quote(self):
        expected = BlockType.QUOTE
        blocks_to_test = [
            "<one line quote>",
            "< text with spaces >",
            "< text with spaces after the closing> ",
            '''<multi>
<line>
<quote>''',
        ]
        for block in blocks_to_test:
            actual = block_to_block_type(block)
            self.assertEqual(actual,expected, msg=f"Expected {expected}, got {actual} on {block}")
        
        expected = BlockType.PARAGRAPH
        blocks_to_fail = [
            "<no closing",
            " no opening quote >",
            " < starting space>",
            '''<multi>
<failed
<quote>''', 
        ]
        for block in blocks_to_fail:
            actual = block_to_block_type(block)
            self.assertEqual(actual,expected, msg=f"Expected {expected}, got {actual} on {block}")