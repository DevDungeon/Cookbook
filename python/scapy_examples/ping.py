from scapy.all import IP, ICMP, send

IP = IP(dst="127.0.0.1")
Ping = ICMP()
send(IP/Ping)