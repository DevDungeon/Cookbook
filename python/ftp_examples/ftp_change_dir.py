from ftplib import FTP

with FTP('ftp.example.com', 'user', 'secret') as ftp:
    print(ftp.cwd('other_dir'))  # Change to `other_dir/`
