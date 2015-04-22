#!/usr/bin/env python
# note that this script requires tcpdump to be installed
# additionally, it requires root privs to run.
# ----
# Portions of this code can be attributed to the book
# Python for Unix and Linux System Administration
# by Noah Gift and Jeremy M. Jones. 
# Copyright 2008 Noah Gift and Jeremy M. Jones
# ISBN-13: 978-0-596-51582-9
# ----

import sys
if len(sys.argv) != 2:
    print "Usage: pingarp \n  eg: pingarp 192.168.1.0/24"
    sys.exit(1)

from scapy.all import srp,Ether,ARP,conf
conf.verb=0
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),
              timeout=2)

print r"MAC,IP"
for snd,rcv in ans:
    print rcv.sprintf(r"%Ether.src%,%ARP.psrc%")