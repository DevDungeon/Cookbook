from scapy.all import IP, ICMP, send

IP = IP(dst="192.168.1.76")
Ping = ICMP()
send(IP/Ping)