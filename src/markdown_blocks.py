def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    final_blocks = []
    for i in range(0, len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] != "":
            final_blocks.append(blocks[i])

    return final_blocks
