#!/usr/bin/python2
import socket
import os
import struct
from ctypes import *

# Host to listen on
host = "192.168.1.4"

# IP Header class
class IP(Structure):
    _fields_ = [
        ("ihl",             c_ubyte, 4),
        ("version",         c_ubyte, 4),
        ("tos",             c_ubyte, 8),
        ("len",             c_ushort, 16),
        ("id",              c_ushort, 16),
        ("offset",          c_ushort, 16),
        ("ttl",             c_ubyte, 8),
        ("protocol_num",    c_ubyte, 8),
        ("sum",             c_ushort, 16),
        ("src",             c_ulong, 32),
        ("dst",             c_ulong, 32)
    ]

    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        # Map protocol constants to names
        self.protocol_map = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        # Human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))

        # Human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)


# Create raw socket and bind
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))

# Include IP headers in capture
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# In windows need to send an IOCTL to set up listen mode
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


try:
    while True:
        # Read in a packet
        raw_buffer = sniffer.recvfrom(65565) [0]

        # Create IP header object from the first 20 bytes
        ip_header = IP(raw_buffer[0:20])

        # Output protocol and hosts detected
        print "Protocol: %s %s -> %s" \
              % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)

except KeyboardInterrupt:
    # Turn off listen mode in windows
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
