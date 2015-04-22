import socket, ssl, pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# require a certificate from the server
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="ca-certs.txt",
                           cert_reqs=1)
ssl_sock.connect(('www.verisign.com', 443))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())


# Set a simple HTTP request -- use httplib in actual code.

ssl_sock.write("""GET / HTTP/1.0\r

Host: www.verisign.com\r\n\r\n""")



# Read a chunk of data.  Will not necessarily

# read all the data returned by the server.

data = ssl_sock.read()



# note that closing the SSLSocket will also close the underlying socket

ssl_sock.close()