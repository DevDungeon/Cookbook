#!/bin/bash


# Check if a path exists (whether file, dir, socket)
if [ -e /path ]; then echo "exists"; fi

# Check if a path exists AND is a file
if [ -f /some/file ]; then echo "exists as file"; else echo "not exist"; fi

# Check if a path exists AND is a dir
if [ -d /some/dir ]; then echo "exists as dir"; else echo "not exist"; fi

# Combining checks with && or ||
if [ ! -f /path && ! -d /path ]; then echo "doesnt exist"; fi

# Create dir with parents
mkdir -p /full/path

# Do something with each file in a dir
for f in *; do echo "$f"; done

# Work on a list of files
for f in file1.txt file2.txt file3.txt; do echo "$f"; done
# or define list of files as a var
FILES="file1.txt
file2.txt
file3.txt"
for f in $FILES; do echo "$f"; done


: '
Checks:
-b FILE - True if the FILE exists and is a special block file.
-c FILE - True if the FILE exists and is a special character file.
-d FILE - True if the FILE exists and is a directory.
-e FILE - True if the FILE exists and is a file, regardless of type (node, directory, socket, etc.).
-f FILE - True if the FILE exists and is a regular file (not a directory or device).
-G FILE - True if the FILE exists and has the same group as the user running the command.
-h FILE - True if the FILE exists and is a symbolic link.
-g FILE - True if the FILE exists and has set-group-id (sgid) flag set.
-k FILE - True if the FILE exists and has a sticky bit flag set.
-L FILE - True if the FILE exists and is a symbolic link.
-O FILE - True if the FILE exists and is owned by the user running the command.
-p FILE - True if the FILE exists and is a pipe.
-r FILE - True if the FILE exists and is readable.
-S FILE - True if the FILE exists and is a socket.
-s FILE - True if the FILE exists and has nonzero size.
-u FILE - True if the FILE exists, and set-user-id (suid) flag is set.
-w FILE - True if the FILE exists and is writable.
-x FILE - True if the FILE exists and is executable
'

