<?php
/**
 * Run PHP Built-in server to serve local files
 *
 * https://www.php.net/manual/en/features.commandline.webserver.php
 *
 * Run with: `php run_local_server.php`
 */

define('EXECUTION_COMMAND', 'php -S localhost:9999 -t ./');// -c ./php.ini');
// define('EXECUTION_COMMAND', 'php -S localhost:9999 -t ./ -c ./php.ini');

// Only allow it to run if it is being executed from the CLI.
// We do not want someone triggering it from a browser, as it will leave a process open forever/clash with IP binding
$executing_server_name = php_sapi_name();
if ($executing_server_name == 'cli') { // Triggered properly via CLI `php`
    echo "Executing: " . EXECUTION_COMMAND . "\n";
    //// exec - Execute an external program
    //// shell_exec - Execute command via shell and return the complete output as a string
    //// passthru - Execute an external program and display raw output
    //// system - Execute an external program and display the output - returns last line of command, and can provide exit code
    exec(EXECUTION_COMMAND); // php [options] -S <addr>:<port> [-t docroot] [router]
//    passthru(EXECUTION_COMMAND); // php [options] -S <addr>:<port> [-t docroot] [router]
} elseif ($executing_server_name == 'cli-server') { // Being served by built-in web server
    echo "Server cannot be run via web server. Run using command-line.";
} else { // Any other situationq
    echo "Server must be run via command-line `php` interpreter.";
}
