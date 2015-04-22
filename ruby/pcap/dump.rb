require 'pcaprub'
SNAPLENGTH = 65535
capture = PCAPRUB::Pcap.open_live('enp4s0', SNAPLENGTH, true, 0)
dumper = capture.dump_open('./dump.pcap')

capture_packets = 10
capture.each do |packet|
  capture.dump(packet.length, packet.length, packet)
  capture_packets -= 1
  if capture_packets == 0
    break
  end
end

capture.dump_close