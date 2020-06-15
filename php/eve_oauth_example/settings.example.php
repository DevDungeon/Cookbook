<?php
/**
 * Change `settings.example.php` to `settings.php` with your variables set.
 */
define('EVE_CLIENT_ID', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'); // Register app at EVE Developer portal
define('EVE_SECRET_KEY', 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); // https://developers.eveonline.com/applications
define('EVE_OAUTH_CALLBACK_URL', 'http://localhost:9999/eve_oauth_example/index.php');
define('EVE_OAUTH_SCOPES', implode(" ", ['esi-characters.read_standings.v1'])); // Space separated list of scopes
define('EVE_LOGIN_SERVER_URL', 'https://login.eveonline.com'); // https://{login,sisilogin}.eveonline.com