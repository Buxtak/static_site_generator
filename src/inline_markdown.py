import re

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("Invalid Markdown syntax: missing closing delimiter")
            for i in range(0, len(parts)):
                if parts[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        temp_text = node.text
        for i in images:
            image_alt = i[0]
            image_link = i[1]
            target = f"![{image_alt}]({image_link})"
            sections = temp_text.split(target, 1)
            if sections[0]:
                node1 = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(node1)

            node2 = TextNode(image_alt, TextType.IMAGE, image_link)
            temp_text = sections[1]
            new_nodes.append(node2)

        if temp_text:
            node1 = TextNode(temp_text, TextType.TEXT)
            new_nodes.append(node1)

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        temp_text = node.text
        for i in links:
            link_alt = i[0]
            link_link = i[1]
            target = f"[{link_alt}]({link_link})"
            sections = temp_text.split(target, 1)
            if sections[0]:
                node1 = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(node1)

            node2 = TextNode(link_alt, TextType.LINK, link_link)
            temp_text = sections[1]
            new_nodes.append(node2)

        if temp_text:
            node1 = TextNode(temp_text, TextType.TEXT)
            new_nodes.append(node1)

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = [node]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
