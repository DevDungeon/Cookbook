import os

def dir_size(root_dir):
    total_size = 0
    for (dirpath, dirs, files) in os.walk(root_dir):
        for filename in files:
            file_size = os.stat(os.path.join(dirpath, filename)).st_size
            total_size += file_size
            print("%s - %s bytes" % (os.path.join(dirpath, filename), file_size))
    print("Total size: %d" % total_size)

if __name__ == '__main__':
    # Get full size of home directory
    dir_size(os.path.expanduser("~"))
