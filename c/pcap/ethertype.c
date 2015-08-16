#include <stdio.h>
#include <pcap.h>
#include <netinet/in.h>
#include <net/ethernet.h>

/* This function can be used as a callback for pcap_loop() */
void my_packet_handler(
    u_char *args,
    const struct pcap_pkthdr* header,
    const u_char* packet
) {
    struct ether_header *eth_header;
    /* The packet is larger than the ether_header struct,
       but we just want to look at the first part of the packet
       that contains the header. We force the compiler
       to treat the pointer to the packet as just a pointer
       to the ether_header. The data payload of the packet comes
       after the headers. Different packet types have different header
       lengths though, but the ethernet header is always the same (14 bytes) */
    eth_header = (struct ether_header *) packet;
    
    if (ntohs(eth_header->ether_type) == ETHERTYPE_IP) {
        printf("IP\n");
    } else  if (ntohs(eth_header->ether_type) == ETHERTYPE_ARP) {
        printf("ARP\n");
    } else  if (ntohs(eth_header->ether_type) == ETHERTYPE_REVARP) {
        printf("Reverse ARP\n");
    }
}

int main(int argc, char **argv) {
    pcap_t *handle;
    char error_buffer[PCAP_ERRBUF_SIZE];
    char *device = "eth0";
    int snapshot_len = 1028;
    int promiscuous = 0;
    int timeout = 1000;

    handle = pcap_open_live(device, snapshot_len, promiscuous, timeout, error_buffer);
    pcap_loop(handle, 1, my_packet_handler, NULL);
    pcap_close(handle);
    return 0;
}