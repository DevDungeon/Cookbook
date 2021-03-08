require 'pcaprub'

pcapfile = File.dirname(__FILE__) + "/dump.pcap"

if(not File.exists?(pcapfile))
  raise RuntimeError, "The PCAP file #{pcapfile} could not be found"
end

capture = ::Pcap.open_offline(pcapfile)

begin
  capture.each do |packet|
    puts packet
  end

# ^C to stop sniffing
rescue Interrupt
  puts "\nPacket Capture stopped by interrupt signal."

rescue Exception => e
  puts "\nERROR: #{e}"
  retry
end

