import shutil

"""
shutil.copyfile("source.txt", "copy.txt")

# Copies permission bits, last access, last modification, flags
# Does not modify owner, group, or file contents
shutil.copystat(src, dst)

shutil.copy2(src, dst) # This is copyfile + copystat

shutil.copytree(src, dst, symlinks=False, ignore=None)
shutil.rmtree(path[, ignore_errors[, onerror]])

shutil.move(src, dst)
"""
