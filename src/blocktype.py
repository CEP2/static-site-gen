from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH       = "paragraph"
    HEADING         = "heading"
    CODE            = "code"
    QUOTE           = "quote"
    UNORDERED_LIST  = "unordered list"
    ORDERED_LIST    = "ordered list"

'''
In: Block of markdown.
Out Block Type designation
Assumptions: Text stripped of whitespace.
'''
def block_to_block_type(block):
    

    

    return BlockType.PARAGRAPH

def is_heading(block):
    # pattern = r'^#{1,6} '
    # if re.search(pattern,block):
    #     return True
    
    lines = block.split()
    for char in lines[0]:
        if char != '#':
            return False
    return True

def is_code(block):
    lines = block.split('\n')
    ticks = '```'
    if lines[0] == ticks and lines[-1] == ticks:
        return True
    return False
    
def is_quote(block):
    pass

