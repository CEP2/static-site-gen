from enum import Enum
import re

MAX_HEADING_HASH_COUNT = 6

class BlockType(Enum):
    PARAGRAPH       = "paragraph"
    HEADING         = "heading"
    CODE            = "code"
    QUOTE           = "quote"
    UNORDERED_LIST  = "unordered list"
    ORDERED_LIST    = "ordered list"

