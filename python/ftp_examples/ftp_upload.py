from ftplib import FTP

with FTP('ftp.example.com', 'user', 'pass') as ftp:
    # For text file
    with open('test.txt', 'rb') as text_file:
        ftp.storlines('STOR test.txt', text_file)

    # For binary file
    with open('image.png', 'rb') as image_file:
        ftp.storbinary('STOR image.png', image_file)