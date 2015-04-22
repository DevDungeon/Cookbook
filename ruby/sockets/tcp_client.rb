require 'socket'

port = 3333

a = TCPSocket.new('127.0.0.1', port) 

a.write "Hello, server!"
puts "Server returned: " + a.recv(1024)

a.close