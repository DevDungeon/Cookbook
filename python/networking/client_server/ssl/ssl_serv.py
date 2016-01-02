import socket
from OpenSSL import SSL

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('key.pem')
context.use_certificate_file('cert.pem')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = SSL.Connection(context, s)
s.bind(('', 12345))
s.listen(5)

(connection, address) = s.accept()
while True:
    print repr(connection.recv(65535))