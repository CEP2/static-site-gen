from blocktype import BlockType

def markdown_to_blocks(markdown):
    #split, then strip all elements.
    block_strings = list(map(str.strip, markdown.split("\n\n")))
    return [b for b in block_strings if b]

'''
In: Block of markdown.
Out Block Type designation
Assumptions: Text stripped of whitespace.
'''
def block_to_block_type(block):
    
    if is_heading(block):
        return BlockType.HEADING
    elif is_code(block):
        return BlockType.CODE
    elif is_quote(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else: 
        return BlockType.PARAGRAPH

def is_heading(block):
    # pattern = r'^#{1,6} '
    # if re.search(pattern,block):
    #     return True
    if block[0] != '#':
        return False
    lines = block.split()
    hashcount = 0
    for char in lines[0]:
        if char != '#':
            return False
        hashcount += 1
        if hashcount > 6:
            return False
    return True

def is_code(block):
    num_lines = len(block.split('\n'))
    ticks = '```'
    if num_lines > 1 and block.startswith(ticks) and block.endswith(ticks):
        return True
    return False
    
def is_quote(block):
    lines = block.split('\n')
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def is_unordered_list(block):
    lines = block.split('\n')
    for line in lines:
        if line.split()[0] != '-':
            return False
    return True

def is_unordered_list(block):
    lines = block.split('\n')
    for line in lines:
        if line.split()[0] != '-':
            return False
    return True

def is_ordered_list(block):
    lines = block.split('\n')
    count = 1
    for line in lines:
        l = line.split()[0]
        if l[-1] != '.':
            return False
        txt_num = l[:-1]
        try: 
            num = int(txt_num) #ValueError if incorrect. 
            if num == count:
                count += 1
            else:
                return False
        except:
            return False
    return True