#!/usr/bin/python2

"""
Captures a single ICMP ping packet
"""

import socket
import os

# Host to listen on
host = "192.168.1.4"

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

# Read single packet
print sniffer.recvfrom(65565)

# Turn off listen mode in windows
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)



