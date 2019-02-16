<?php

$socket = stream_socket_client("ssl://192.168.1.96:8000", $errno, $errstr);

if ($socket) {
	echo fread($socket, 2000);
}

