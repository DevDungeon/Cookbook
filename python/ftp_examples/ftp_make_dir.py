from ftplib import FTP

with FTP('ftp.example.com', 'user', 'secret') as ftp:
    ftp.mkd('my_new_dir')
