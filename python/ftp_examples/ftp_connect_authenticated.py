from ftplib import FTP

# Connect and login at once
with FTP(host='ftp.example.com', user='me', passwd='secret') as ftp:
    print(ftp.getwelcome())

# Or connect and login as separate steps
ftp = FTP()
ftp.connect('ftp.example.com', 21)
ftp.login('me', 'secret')
print(ftp.getwelcome())
ftp.close()