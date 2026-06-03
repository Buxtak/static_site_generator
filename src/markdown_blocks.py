from enum import Enum


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    final_blocks = []
    for i in range(0, len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] != "":
            final_blocks.append(blocks[i])

    return final_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block_node):
    lines = block_node.split("\n")
    index = 0
    if block_node.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if lines[0].startswith("```") and lines[-1].startswith("```") and len(lines) > 1:
        return BlockType.CODE

    if block_node.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block_node.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    if block_node.startswith("1. "):
        for line in lines:
            index += 1
            if not line.startswith(f"{index}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
