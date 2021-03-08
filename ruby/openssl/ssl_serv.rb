require 'socket'
require 'openssl'

# Key 
key = OpenSSL::PKey::RSA.new 2048

# Certificate
name = OpenSSL::X509::Name.parse 'CN=nobody/DC=example'
cert = OpenSSL::X509::Certificate.new
cert.version = 2
cert.serial = 0
cert.not_before = Time.now
cert.not_after = Time.now + 3600
cert.public_key = key.public_key
cert.subject = name

# SSL Context
context = OpenSSL::SSL::SSLContext.new
context.cert = cert
context.key = key

# TCP Server
tcp_server = TCPServer.new 5000
ssl_server = OpenSSL::SSL::SSLServer.new tcp_server, context

loop do
  connection = ssl_server.accept

  data = connection.gets

  response = "I got #{data.dump}"
  puts response

  connection.puts "I got #{data.dump}"
  connection.close
end