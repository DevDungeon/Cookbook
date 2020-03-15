from ftplib import FTP, all_errors

with FTP('ftp.example.com', 'user', 'pass') as ftp:
        
    # For text files
    with open('local_test.txt', 'w') as local_file:  # Open local file for writing
        # Download `test.txt` from server and write to `local_file`
        # Pass absolute or relative path
        response = ftp.retrlines('RETR test.txt', local_file.write)

        # Check the response code
        # https://en.wikipedia.org/wiki/List_of_FTP_server_return_codes
        if response.startswith('226'):  # Transfer complete
            print('Transfer complete')
        else:
            print('Error transferring. Local file may be incomplete or corrupt.')
        
    # For binary use `retrbinary()`
    with open('image.png', 'wb') as local_file:
        ftp.retrbinary('RETR image.png', local_file.write)
        