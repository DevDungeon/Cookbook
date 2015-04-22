package main

import (
	"code.google.com/p/gopacket"
	"code.google.com/p/gopacket/pcap"
	"fmt"
	//	"net"
)

func main() {

	if handle, err := pcap.OpenLive("eth0", 1600, true, 0); err != nil {
		panic(err)
	} else if err := handle.SetBPFFilter("tcp and port 80"); err != nil { // optional
		panic(err)
	} else {
		packetSource := gopacket.NewPacketSource(handle, handle.LinkType())
		var packetCount int
		for packet := range packetSource.Packets() {
			
			//handlePacket(packet)  // Do something with a packet here.
			//fmt.Println(packet)

			packetCount++
			fmt.Printf("Total packet count: %d\n", packetCount)

			packetAppLayer := packet.ApplicationLayer()
			if packetAppLayer == nil {
				fmt.Println("packet.ApplicationLayer() is nil")
			} else {
				fmt.Printf("packetAppLayer type: %T", packetAppLayer)
				payload := packetAppLayer.Payload()
				if payload == nil {
					fmt.Printf("Payload is nil")
				} else {
					fmt.Printf("Payload ========================\n%s============================\n", payload)
				}
			}
		}
	}

}
