from ftplib import FTP

with FTP('ftp.example.com', 'user', 'secret') as ftp:
    # List files
    files = []
    ftp.dir(files.append)  # Takes a callback for each file
    for f in files:
        print(type(f))
        print(f)
