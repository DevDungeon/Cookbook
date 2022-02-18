<?php
/**
 * Router
 */

// To run locally:
//    cd public/
//    php -S localhost:9000 index.php

// To run with .htaccess:
/*
# .htaccess
RewriteEngine On
RewriteBase /
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.+)$ index.php [QSA,L]
*/

// Include any other global functions
require '../controller/helpers/functions.php';


/**
 * Handle routing. Pass control to a "controller"
 */

// Some $_SERVER keys:
// - REQUEST_URI
// - REQUEST_METHOD  GET
// - QUERY_STRING
// - HTTPS
switch ($_SERVER['REQUEST_URI']) {
    case '':
    case '/':
        // To render a static page, pass control directly
        // to the template. No need for a controller.
        require '../view/php/hello.tpl.php';
        break;
	case '/view-post/4':
		require '../controller/view-post.php';
		break;
  default:
	    http_response_code(404);
	    echo '<html><body>404 Not Found</body></html>';
	    break;
}
