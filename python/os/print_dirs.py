# print_dirs.py
import os

def print_dirs_recursively(root_dir):
    root_dir = os.path.abspath(root_dir)
    print(root_dir)

    for item in os.listdir(root_dir):
        item_full_path = os.path.join(root_dir, item)
        if os.path.isdir(item_full_path):
            print_dirs_recursively(item_full_path)