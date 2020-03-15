from ftplib import FTP, all_errors

with FTP('ftp.example.com', 'user', 'pass') as ftp:
    try:
        ftp.rename('test.txt', 'my_file.txt')
    except all_errors as error:
        print(f'Error renaming file on server: {error}')
