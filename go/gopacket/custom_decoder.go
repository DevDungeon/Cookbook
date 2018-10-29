package main

import (
	"fmt"
	"github.com/google/gopacket"
)

// Create custom layer structure
type CustomLayer struct {
	// This layer just has two bytes at the front
	SomeByte    byte
	AnotherByte byte
	restOfData  []byte
}

// Register the layer type so we can use it
// The first argument is an ID. Use negative
// or 2000+ for custom layers. It must be unique
var CustomLayerType = gopacket.RegisterLayerType(
	2001,
	gopacket.LayerTypeMetadata{
		"CustomLayerType",
		gopacket.DecodeFunc(decodeCustomLayer),
	},
)

// When we inquire about the type, what type of layer should
// we say it is? We want it to return our custom layer type
func (l CustomLayer) LayerType() gopacket.LayerType {
	return CustomLayerType
}

// LayerContents returns the information that our layer
// provides. In this case it is a header layer so
// we return the header information
func (l CustomLayer) LayerContents() []byte {
	return []byte{l.SomeByte, l.AnotherByte}
}

// LayerPayload returns the subsequent layer built
// on top of our layer or raw payload
func (l CustomLayer) LayerPayload() []byte {
	return l.restOfData
}

// Custom decode function. We can name it whatever we want
// but it should have the same arguments and return value
// When the layer is registered we tell it to use this decode function
func decodeCustomLayer(data []byte, p gopacket.PacketBuilder) error {
	// AddLayer appends to the list of layers that the packet has
	p.AddLayer(&CustomLayer{data[0], data[1], data[2:]})

	// The return value tells the packet what layer to expect
	// with the rest of the data. It could be another header layer,
	// nothing, or a payload layer.

	// nil means this is the last layer. No more decoding
	// return nil

	// Returning another layer type tells it to decode
	// the next layer with that layer's decoder function
	// return p.NextDecoder(layers.LayerTypeEthernet)

	// Returning payload type means the rest of the data
	// is raw payload. It will set the application layer
	// contents with the payload
	return p.NextDecoder(gopacket.LayerTypePayload)
}

func main() {
	// If you create your own encoding and decoding you can essentially
	// create your own protocol or implement a protocol that is not
	// already defined in the layers package. In our example we are just
	// wrapping a normal ethernet packet with our own layer.
	// Creating your own protocol is good if you want to create
	// some obfuscated binary data type that was difficult for others
	// to decode

	// Finally, decode your packets:
	rawBytes := []byte{0xF0, 0x0F, 65, 65, 66, 67, 68}
	packet := gopacket.NewPacket(
		rawBytes,
		CustomLayerType,
		gopacket.Default,
	)
	fmt.Println("Created packet out of raw bytes.")
	fmt.Println(packet)

	// Decode the packet as our custom layer
	customLayer := packet.Layer(CustomLayerType)
	if customLayer != nil {
		fmt.Println("Packet was successfully decoded with custom layer decoder.")
		customLayerContent, _ := customLayer.(*CustomLayer)
		// Now we can access the elements of the custom struct
		fmt.Println("Payload: ", customLayerContent.LayerPayload())
		fmt.Println("SomeByte element:", customLayerContent.SomeByte)
		fmt.Println("AnotherByte element:", customLayerContent.AnotherByte)

	}
}
