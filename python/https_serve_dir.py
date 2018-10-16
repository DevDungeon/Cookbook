# Sets up an HTTPS server that serves directory contents

# Generate a private key and certificate using openssl:
# openssl req -newkey rsa:2048 -nodes -keyout privkey.pem -x509 -days 36500 -out certificate.pem -subj "/C=US/ST=NRW/L=Earth/O=CompanyName/OU=IT/CN=www.example.com/emailAddress=email@example.com"

import sys
import ssl

listen_target = ('localhost', 4443)
certificate_file = './certificate.pem'
private_key_file = './privkey.pem'

# Python 3 version
if sys.version_info[0] == 3:
    import http.server
    httpd = http.server.HTTPServer(listen_target, http.server.SimpleHTTPRequestHandler)
# Python 2 version
elif sys.version_info[0] == 2:
    import BaseHTTPServer, SimpleHTTPServer
    httpd = BaseHTTPServer.HTTPServer(listen_target, SimpleHTTPServer.SimpleHTTPRequestHandler)

# Wrap the socket with SSL
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certificate_file, keyfile=private_key_file, server_side=True)

# Start listening
httpd.serve_forever()
