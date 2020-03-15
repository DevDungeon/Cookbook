from ftplib import FTP

with FTP('ftp.example.com', 'user', 'secret') as ftp:
    print(ftp.pwd())  # Usually default is /

