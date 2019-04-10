import os

def copy_dir_recursively(source_dir, target_dir):
    for (dirpath, dirs, files) in os.walk(source_dir):
        for dir in dirs:
            os.mkdir()