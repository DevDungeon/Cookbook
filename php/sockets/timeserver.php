<?php
$socket = stream_socket_server("tcp://192.168.1.96:8000", $errno, $errstr);
if (!$socket) {
  echo "$errstr ($errno)<br />\n";
} else {
while(1) {
  while ($conn = stream_socket_accept($socket, -1, $peername)) {
    fwrite($conn, 'The local time is ' . date('n/j/Y g:i a') . "\n");
    print "Peer: $peername\n";
    fclose($conn);
  }
  echo 'relooping';
}
  fclose($socket);
}
?>

