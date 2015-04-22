require 'socket'

socket = UDPSocket.new

data = 'Some data to send'

socket.send(data, 0, '127.0.0.1', 4444)
socket.close