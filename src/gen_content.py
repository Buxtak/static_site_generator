import os
from pathlib import Path

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    title = ""
    count_title = 0

    for line in lines:
        if line.startswith("# "):
            title = line[2:]
            count_title += 1
            break
    if count_title > 0:
        return title
    else:
        raise Exception("No title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    md_file = open(from_path, "r")
    markdown = md_file.read()
    md_file.close()

    temp_file = open(template_path, "r")
    template = temp_file.read()
    temp_file.close()

    md_node = markdown_to_html_node(markdown)
    html_string = md_node.to_html()
    title = extract_title(markdown)

    tem_w_title = template.replace("{{ Title }}", title)
    temp_w_content = tem_w_title.replace("{{ Content }}", html_string)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    new_file = open(dest_path, "w")
    new_file.write(temp_w_content)
    new_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)
    for dir in dirs:
        file_dir = os.path.join(dir_path_content, dir)
        dest = os.path.join(dest_dir_path, dir)
        if os.path.isfile(file_dir):
            html_dest = Path(dest).with_suffix(".html")
            generate_page(file_dir, template_path, html_dest)
        else:
            generate_pages_recursive(file_dir, template_path, dest)
