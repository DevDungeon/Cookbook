from ftplib import FTP, all_errors

with FTP('ftp.example.com', 'user', 'pass') as ftp:
    try:
        ftp.delete('test.txt')
    except all_errors as error:
        print(f'Error deleting file: {error}') 
