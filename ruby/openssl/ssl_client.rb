require 'socket'
require 'openssl'

# SSL Context - Client does not require cert/key if not being verified
context = OpenSSL::SSL::SSLContext.new
#context.cert = cert
#context.key = key

# TCP Client
tcp_client = TCPSocket.new 'localhost', 5000
ssl_client = OpenSSL::SSL::SSLSocket.new tcp_client, context
ssl_client.connect

ssl_client.puts "hello server!"
puts ssl_client.gets