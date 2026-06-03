import re

from img_link_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


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
