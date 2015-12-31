#!/usr/bin/python
from scapy.all import *

ip=IP(src="192.168.1.76", dst="192.168.1.64")
SYN=TCP(sport=1500, dport=80, flags="S", seq=100)
SYNACK=sr1(ip/SYN)

my_ack = SYNACK.seq + 1
ACK=TCP(sport=1050, dport=80, flags="A", seq=101, ack=my_ack)
send(ip/ACK)

payload="stuff"
PUSH=TCP(sport=1050, dport=80, flags="PA", seq=11, ack=my_ack)
send(ip/PUSH/payload)