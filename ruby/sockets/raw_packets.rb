# https://gist.githubusercontent.com/KINGSABRI/2898001/raw/f13cdb897ce24613647c9020aedded6a6c26f412/syn-poc.rb
# Untested
#

#!/usr/bin/env ruby
# Full Contol on Ethnet, IP & TCP headers. Play with it ;)
# to test it: nc -lvp 4444
# as root: tcpdump  -nvvvv 'tcp port 4444' -i wlan0  # change wlan0 to your interface
# or use packetfu to monitor as tcpdump
## cap = PacketFu::Capture.new(:iface => 'wlan0' , :promisc=> true)
## cap.show_live(:filter => 'tcp and port 4444')
# libpcap should be installed
# gem install pcaprub packetfu


=begin


		      # IP header format
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version|  IHL  |Type of Service|          Total Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Identification        |Flags|      Fragment Offset    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Time to Live |    Protocol   |         Header Checksum       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                       Source Address                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Destination Address                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   http://www.ietf.org/rfc/rfc0791.txt



		      # TCP header format
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |          Source Port          |       Destination Port        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        Sequence Number                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Acknowledgment Number                      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Data |           |U|A|P|R|S|F|                               |
   | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
   |       |           |G|K|H|T|N|N|                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Checksum            |         Urgent Pointer        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             data                              |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   http://www.ietf.org/rfc/rfc793.txt


=end

require 'packetfu'

def pkts
    $config = PacketFu::Config.new(PacketFu::Utils.whoami?(:iface=> "wlan0")).config 	# set interface
    #$config = PacketFu::Config.new(:iface=> "wlan0").config   # use this line instead of above if you face `whoami?': uninitialized constant PacketFu::Capture (NameError)

    #--> Build TCP/IP

    #- Build Ethernet header:---------------------------------------
    pkt = PacketFu::TCPPacket.new(:config => $config , :flavor => "Linux")		# IP header
    #     pkt.eth_src = "00:11:22:33:44:55"			# Ether header: Source MAC ; you can use: pkt.eth_header.eth_src
    #     pkt.eth_dst = "FF:FF:FF:FF:FF:FF"			# Ether header: Destination MAC ; you can use: pkt.eth_header.eth_dst
    pkt.eth_proto					# Ether header: Protocol ; you can use: pkt.eth_header.eth_proto
    #- Build IP header:---------------------------------------
    pkt.ip_v      = 4					# IP header: IPv4 ; you can use: pkt.ip_header.ip_v
    pkt.ip_hl     = 5					# IP header: IP header length ; you can use: pkt.ip_header.ip_hl
    pkt.ip_tos	  = 0					# IP header: Type of service ; you can use: pkt.ip_header.ip_tos
    pkt.ip_len	  = 20					# IP header: Total Length ; you can use: pkt.ip_header.ip_len
    pkt.ip_id						# IP header: Identification ; you can use: pkt.ip_header.ip_id
    pkt.ip_frag   = 0					# IP header: Don't Fragment ; you can use: pkt.ip_header.ip_frag
    pkt.ip_ttl    = 115					# IP header: TTL(64) is the default ; you can use: pkt.ip_header.ip_ttl
    pkt.ip_proto  = 6					# IP header: Protocol = tcp (6) ; you can use: pkt.ip_header.ip_proto
    pkt.ip_sum						# IP header: Header Checksum ; you can use: pkt.ip_header.ip_sum
    pkt.ip_saddr    = "2.2.2.2"				# IP header: Source IP. use $config[:ip_saddr] if you want your real IP ; you can use: pkt.ip_header.ip_saddr
    pkt.ip_daddr    = "10.20.50.45"			# IP header: Destination IP ; you can use: pkt.ip_header.ip_daddr
    #- TCP header:---------------------------------------
    pkt.payload   = "Hacked!"				# TCP header: packet header(body)
    pkt.tcp_flags.ack  = 0				# TCP header: Acknowledgment
    pkt.tcp_flags.fin  = 0				# TCP header: Finish
    pkt.tcp_flags.psh  = 0				# TCP header: Push
    pkt.tcp_flags.rst  = 0				# TCP header: Reset
    pkt.tcp_flags.syn  = 1				# TCP header: Synchronize sequence numbers
    pkt.tcp_flags.urg  = 0				# TCP header: Urgent pointer
    pkt.tcp_ecn        = 0				# TCP header: ECHO
    pkt.tcp_win	       = 8192				# TCP header: Window
    pkt.tcp_hlen       = 5				# TCP header: header length
    pkt.tcp_src        = 5555				# TCP header: Source Port (random is the default )
    pkt.tcp_dst        = 4444				# TCP header: Destination Port (make it random/range for general scanning)
    pkt.recalc						# Recalculate/re-build whol pkt (should be at the end)

    #--> End of Build TCP/IP

    pkt_to_a = [pkt.to_s]
    return pkt_to_a
end


def scan
    pkt_array = pkts.sort_by{rand}
    puts "-" * " [-] Send Syn flag".length + "\n"  + " [-] Send Syn flag " + "\n"

    inj = PacketFu::Inject.new(:iface => $config[:iface] , :config => $config, :promisc => false)
    inj.array_to_wire(:array => pkt_array)		# Send/Inject the packet through connection

    puts " [-] Done" + "\n" + "-" * " [-] Send Syn flag".length
end

scan