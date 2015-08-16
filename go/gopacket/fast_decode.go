package main

import (
    "fmt"
    "github.com/google/gopacket"
    "github.com/google/gopacket/layers"
    "github.com/google/gopacket/pcap"
    "log"
    "time"
)

var (
    device       string = "eth0"
    snapshot_len int32  = 1024
    promiscuous  bool   = false
    err          error
    timeout      time.Duration = 30 * time.Second
    handle       *pcap.Handle
    // Will reuse these for each packet
    ethLayer layers.Ethernet
    ipLayer  layers.IPv4
    tcpLayer layers.TCP
)

func main() {
    // Open device
    handle, err = pcap.OpenLive(device, snapshot_len, promiscuous, timeout)
    if err != nil {
        log.Fatal(err)
    }
    defer handle.Close()

    packetSource := gopacket.NewPacketSource(handle, handle.LinkType())
    for packet := range packetSource.Packets() {

        // Do something with a packet here.

        parser := gopacket.NewDecodingLayerParser(
            layers.LayerTypeEthernet,
            &ethLayer,
            &ipLayer,
            &tcpLayer,
        )
        decoded := []gopacket.LayerType{}

        err := parser.DecodeLayers(packet.Data(), &decoded)
        if err != nil {
            fmt.Println("Trouble decoding layers: ", err)
        }

        for _, layerType := range decoded {
            if layerType == layers.LayerTypeIPv4 {
                fmt.Println("IPv4: ", ipLayer.SrcIP, "->", ipLayer.DstIP)
            }
            if layerType == layers.LayerTypeTCP {
                fmt.Println("TCP Port: ", tcpLayer.SrcPort, "->", tcpLayer.DstPort)
                fmt.Println("TCP SYN:", tcpLayer.SYN, " | ACK:", tcpLayer.ACK)
            }
        }
    }

}
