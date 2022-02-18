<?php

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
        require 'view/hello.php';
        break;
	case '/view-post/4':
		require 'controller/view-post.php';
		break;
  default:
	    http_response_code(404);
	    echo '<html><body>404 Not Found</body></html>';
	    break;
}