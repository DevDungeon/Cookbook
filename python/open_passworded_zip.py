from zipfile import ZipFile

with ZipFile('file.zip') as my_zip_file:
    my_zip_file.extractall(pwd='secret')