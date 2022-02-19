<?php
/**

The $_SERVER superglobal
https://www.php.net/manual/en/reserved.variables.server.php

*/
?>
<html>
<body>
<pre>

<?php
// https://www.php.net/manual/en/language.variables.superglobals.php
print_r($_SERVER);
print_r($_FILES);
print_r($_GET);
print_r($_POST);
print_r($_COOKIE);
print_r($_SESSION);
print_r($_REQUEST);
print_r($_ENV);


?>

<?php /*
Example output of $_SERVER:


Array
(
    [DOCUMENT_ROOT] => /home/odin/Cookbook/php/devops_debug
    [REMOTE_ADDR] => ::1
    [REMOTE_PORT] => 57202
    [SERVER_SOFTWARE] => PHP 7.4.25 Development Server
    [SERVER_PROTOCOL] => HTTP/1.1
    [SERVER_NAME] => localhost
    [SERVER_PORT] => 9000
    [REQUEST_URI] => /superglobals.php
    [REQUEST_METHOD] => GET
    [SCRIPT_NAME] => /superglobals.php
    [SCRIPT_FILENAME] => /home/nanodano/Cookbook/php/devops_debug/superglobals.php
    [PHP_SELF] => /superglobals.php
    [HTTP_HOST] => localhost:9000
    [HTTP_USER_AGENT] => Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
    [HTTP_ACCEPT] => text/html,application/xhtml+xml;q=0.8
    [HTTP_ACCEPT_LANGUAGE] => en-US,en;q=0.5
    [HTTP_ACCEPT_ENCODING] => gzip, deflate
    [HTTP_CONNECTION] => keep-alive
    [HTTP_COOKIE] => asdf
    [HTTP_UPGRADE_INSECURE_REQUESTS] => 1
    [HTTP_SEC_FETCH_DEST] => document
    [HTTP_SEC_FETCH_MODE] => navigate
    [HTTP_SEC_FETCH_SITE] => none
    [HTTP_SEC_FETCH_USER] => ?1
    [HTTP_CACHE_CONTROL] => max-age=0
    [REQUEST_TIME_FLOAT] => 1645036482.9527
    [REQUEST_TIME] => 1645036482
)
*/
?>

</pre>
</body>
</html>
