from ftplib import FTP

with FTP('ftp.example.com') as ftp:
    print(ftp.getwelcome())