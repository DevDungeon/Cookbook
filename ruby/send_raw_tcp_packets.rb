# https://stackoverflow.com/questions/27162658/is-there-a-simple-way-to-send-a-packet-over-a-raw-socket-using-rubys-socket-cla
# untested
#
#
#
# sock.write [0x03, 0x00, 0x00, 0x16,
#          0x11, 0xE0, 0x00, 0x00, 0x00,
#          0x01, 0x00, 0xC1, 0x02, 0x02,
#          0x02, 0xC2, 0x02, 0x02, 0x02,
#          0xC0, 0x01, 0x0A ].pack('C*')
#
require 'socket'

interface = 'lo'         # loopback interface
interface_index = 0x8933 # SIOCGIFINDEX
frame = "\x00\x1f\xc6\x51\x07\x07\x07"

socket = Socket.new(Socket::AF_PACKET, Socket::SOCK_RAW, Socket::IPPROTO_RAW)
ifreq = [interface.dup].pack 'a*'
socket.ioctl(interface_index, ifreq)
socket.bind([Socket::AF_PACKET].pack('s') + [Socket::IPPROTO_RAW].pack('n') + ifreq[16..20]+ ("\x00" * 12))

socket.send(frame, 0)