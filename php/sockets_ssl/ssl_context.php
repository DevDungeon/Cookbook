

$context = stream_context_create();


// local_cert must be in PEM format
stream_context_set_option($context, 'ssl', 'local_cert', $pemfile);
// Pass Phrase (password) of private key
stream_context_set_option($context, 'ssl', 'passphrase', $pem_passphrase);
stream_context_set_option($context, 'ssl', 'allow_self_signed', true);
stream_context_set_option($context, 'ssl', 'verify_peer', false);

// Create the server socket
$server = stream_socket_server('ssl://0.0.0.0:9001', $errno, $errstr, STREAM_SERVER_BIND|STREAM_SERVER_LISTEN, $context);

