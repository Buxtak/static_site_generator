import os
import shutil

from gen_content import generate_pages_recursive


def main():
    cleaner("public")
    copier("static", "public")
    generate_pages_recursive("content", "template.html", "public")


def cleaner(path_public):
    if os.path.exists(path_public):
        shutil.rmtree(path_public)
    os.mkdir(path_public)


def copier(path_static, path_public):
    for filename in os.listdir(path_static):
        from_path = os.path.join(path_static, filename)
        dest_path = os.path.join(path_public, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            os.mkdir(dest_path)
            copier(from_path, dest_path)


main()
