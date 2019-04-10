import os

def recurse_dir(root_dir):
    root_dir = os.path.abspath(root_dir)
    for item in os.listdir(root_dir):
        item_full_path = os.path.join(root_dir, item)

        if os.path.isdir(item_full_path):
            recurse_dir(item_full_path)
        else:
            print("%s - %s bytes" % (item_full_path, os.stat(item_full_path).st_size))