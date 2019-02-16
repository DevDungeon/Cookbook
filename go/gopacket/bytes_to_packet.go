package main

import (
	"fmt"
	"github.com/google/gopacket"
	"github.com/google/gopacket/layers"
)

func main() {
	// If we don't have a handle to a device or a file, but we have a bunch
	// of raw bytes, we can try to decode them in to packet information

	// NewPacket() takes the raw bytes that make up the packet as the first parameter
	// The second parameter is the lowest level layer you want to decode. It will
	// decode that layer and all layers on top of it. The third layer
	// is the type of decoding: default(all at once), lazy(on demand), and NoCopy
	// which will not create a copy of the buffer

	// Create an packet with ethernet, IP, TCP, and payload layers
	// We are creating one we know will be decoded properly but
	// your byte source could be anything. If any of the packets
	// come back as nil, that means it could not decode it in to
	// the proper layer (malformed or incorrect packet type)
	payload := []byte{2, 4, 6}
	options := gopacket.SerializeOptions{}
	buffer := gopacket.NewSerializeBuffer()
	gopacket.SerializeLayers(buffer, options,
		&layers.Ethernet{},
		&layers.IPv4{},
		&layers.TCP{},
		gopacket.Payload(payload),
	)
	rawBytes := buffer.Bytes()

	// Decode an ethernet packet
	ethPacket :=
		gopacket.NewPacket(
			rawBytes,
			layers.LayerTypeEthernet,
			gopacket.Default,
		)

	// with Lazy decoding it will only decode what it needs when it needs it
	// This is not concurrency safe. If using concurrency, use default
	ipPacket :=
		gopacket.NewPacket(
			rawBytes,
			layers.LayerTypeIPv4,
			gopacket.Lazy,
		)

	// With the NoCopy option, the underlying slices are referenced
	// directly and not copied. If the underlying bytes change so will
	// the packet
	tcpPacket :=
		gopacket.NewPacket(
			rawBytes,
			layers.LayerTypeTCP,
			gopacket.NoCopy,
		)

	fmt.Println(ethPacket)
	fmt.Println(ipPacket)
	fmt.Println(tcpPacket)
}
