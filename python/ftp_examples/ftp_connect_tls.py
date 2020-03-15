from ftplib import FTP_TLS

# Connect to server using TLS, port 21 default. Is not SFTP over SSH
with FTP_TLS('ftp.example.com', 'user', 'secret') as ftp:
    print(ftp.getwelcome())
