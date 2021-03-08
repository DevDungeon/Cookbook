require 'socket'

port = 3333
a = TCPServer.new('', port)

loop {
	connection = a.accept
	puts "Received: " + connection.recv(1024)
	connection.write 'Thank you for sending your message'
	connection.close
}