require 'socket'

BasicSocket.do_not_reverse_lookup = true

client = UDPSocket.new
client.bind('0.0.0.0', 4444)

# If receive buffer is too small, message will be dropped and never seen
data, addr = client.recvfrom(1024) 
puts "From addr: '%s', msg: '%s'" % [addr.join(','), data]
client.close