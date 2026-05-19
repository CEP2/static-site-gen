def markdown_to_blocks(markdown):
    #split, then strip all elements.
    block_strings = list(map(str.strip, markdown.split("\n\n")))
    return [b for b in block_strings if b]
