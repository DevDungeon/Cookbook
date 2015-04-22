<?php

// PHP 5.4 provides a built in web server and can be executed with
// php -S localhost:8888 

// Specify docroot
// php -S 0.0.0.0:8080 -t /path/to/docroot

// Specify file to serve
// php -S 127.0.0.1:8080 file_to_serve.php

// Specify php.ini file
// php -S localhost:9999 -c custom-php.ini

if (php_sapi_name() == 'cli-server') {
	echo "Command line server detected\n";
} else {
	echo "Command line server not detected\n";
}
