<?php

/*

https://www.php.net/manual/en/features.file-upload.php

Some php.ini values that may affect file uploads:

```
file_uploads = On 
upload_max_filesize 40M
max_file_uploads
post_max_size 40M
memory_limit 32M
max_input_time
max_execution_time
upload_tmp_dir
```

## To set PHP INI values in .htaccess, add like this in .htaccess

```
php_value upload_max_filesize 10M
php_value post_max_size 20M
php_value memory_limit 32M
```

## The $_FILES superglobal:

$_FILES['userfile']['name']
    The original name of the file on the client machine.
    
$_FILES['userfile']['type']
    The mime type of the file, if the browser provided this information. An example would be "image/gif". This mime type is however not checked on the PHP side and therefore don't take its value for granted.
    
$_FILES['userfile']['size']
    The size, in bytes, of the uploaded file.
    
$_FILES['userfile']['tmp_name']
    The temporary filename of the file in which the uploaded file was stored on the server.
    
$_FILES['userfile']['error']
    The error code associated with this file upload.

$_FILES['userfile']['full_path']
    The full path as submitted by the browser. This value does not always contain a real directory structure, and cannot be trusted. Available as of PHP 8.1.0.

*/

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	print_r($_FILES);
	if (is_uploaded_file($_FILES['userfile']['tmp_name'])) {
	   echo "File ". $_FILES['userfile']['name'] ." uploaded successfully.\n";
	   echo "Displaying contents\n";
	   readfile($_FILES['userfile']['tmp_name']);
	} else {
	   echo "Possible file upload attack: ";
	   echo "filename '". $_FILES['userfile']['tmp_name'] . "'.";
	}
}


/* To move the uploaded file out of the tmp dir and permanently store it: */
//$uploads_dir = '/uploads';
//foreach ($_FILES["userfile"]["error"] as $key => $error) {
//    if ($error == UPLOAD_ERR_OK) {
//        $tmp_name = $_FILES["pictures"]["tmp_name"][$key];
//        // basename() may prevent filesystem traversal attacks;
//        // further validation/sanitation of the filename may be appropriate
//        $name = basename($_FILES["pictures"]["name"][$key]);
//        move_uploaded_file($tmp_name, "$uploads_dir/$name");
//    }
//}

?>
<html><body>

<form enctype="multipart/form-data" method="POST">
    <!-- MAX_FILE_SIZE must precede the file input field -->
    <input type="hidden" name="MAX_FILE_SIZE" value="30000" />
    <!-- Name of input element determines name in $_FILES array -->
    Send this file: <input name="userfile" type="file" />
    <input type="submit" value="Send File" />
</form>

</body></html>
