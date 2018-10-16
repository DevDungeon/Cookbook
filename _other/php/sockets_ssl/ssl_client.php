<?php

$host = '192.168.1.71';
$port = 9001;
$timeout = 10;
$cert = 'e:\www\workspace\php\sockets\server.pem';


$context = stream_context_create(array('ssl'=>array('local_cert'=> $cert,
)));
if ($fp = stream_socket_client('ssl://'.$host.':'.$port, $errno, $errstr, 30,
        STREAM_CLIENT_CONNECT, $context)) {
    fwrite($fp, "\n");
    echo fread($fp,8192);
    fclose($fp);
} else {
   echo "ERROR: $errno - $errstr<br />\n";
}

?>

