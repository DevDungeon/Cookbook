require 'rubygems'
require 'pcaprub'

#dev = PCAPRUB::Pcap.lookupdev
dev = "enp4s0"
snaplength = 65535
promiscous_mode = true 
timeout = 0 

capture = ::Pcap.open_live(dev, snaplength, promiscous_mode, timeout)

capture.each do |packet|
	p packet
end
