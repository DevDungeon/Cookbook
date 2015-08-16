#include <stdio.h>
#include <time.h>
#include <pcap.h>
#include <netinet/in.h>
#include <netinet/if_ether.h>

void print_packet_info(const u_char *packet, struct pcap_pkthdr packet_header);

int main(int argc, char *argv[]) {
	char *device;
    char error_buffer[PCAP_ERRBUF_SIZE];
	pcap_t *handle;
    const u_char *packet;
 	struct pcap_pkthdr packet_header;
    int packet_count_limit = 1;
    int timeout_limit = 10000; /* In milliseconds */

	device = pcap_lookupdev(error_buffer);
    if (device == NULL) {
        printf("Error finding device: %s\n", error_buffer);
        return 1;
    }

	/* Open device for live capture */
	handle = pcap_open_live(
        device,
        BUFSIZ,
        packet_count_limit,
        timeout_limit,
        error_buffer
    );
	if (handle == NULL) {
		 fprintf(stderr, "Could not open device %s: %s\n", device, error_buffer);
		 return 2;
 	}

 	/* Attempt to capture one packet. If there is no network traffic
      and the timeout is reached, it will return NULL */
 	packet = pcap_next(handle, &packet_header);
 	if (packet == NULL) {
        printf("No packet found.\n");
        return 2;
    }

    /* Our function to output some info */
    print_packet_info(packet, packet_header);

	return 0;
}

void print_packet_info(const u_char *packet, struct pcap_pkthdr packet_header) {
    u_char *pointer;
    int address_length;

    printf(
        "Time recieved: %s\n",
        ctime((const time_t*)&packet_header.ts.tv_sec)
    );
    printf("Packet length %d\n", packet_header.len);
    printf("Packet capture length: %d\n", packet_header.caplen);

    /* What type of ethernet packet */
    struct ether_header *ethernet_header;
    ethernet_header = (struct ether_header *) packet;
    if (ntohs(ethernet_header->ether_type) == ETHERTYPE_IP) {
        printf(
            "Ethernet type hex:%x dec:%d is an IP packet.\n",
            ntohs(ethernet_header->ether_type),
            ntohs(ethernet_header->ether_type)
        );
    } else  if (ntohs (ethernet_header->ether_type) == ETHERTYPE_ARP) {
        printf(
            "Ethernet type hex:%x dec:%d is an ARP packet.\n",
            ntohs(ethernet_header->ether_type),
            ntohs(ethernet_header->ether_type)
        );
    } else {
        printf("Other ethernet type: %x", ntohs(ethernet_header->ether_type));
        return;
    }

    /* Source address */
    address_length = ETHER_ADDR_LEN;
    pointer = ethernet_header->ether_shost;
    printf("Source Address:  ");
    do {
        printf(
            "%s%x",
            (address_length == ETHER_ADDR_LEN) ? " " : ":", *pointer++
        );
    } while(--address_length > 0);
    printf("\n");

    /* Destination address */
    pointer = ethernet_header->ether_dhost;
    address_length = ETHER_ADDR_LEN;
    printf("Destination Address:  ");
    do {
        printf(
            "%s%x",
            (address_length == ETHER_ADDR_LEN) ? " " : ":", *pointer++
        );
    } while(--address_length > 0);
    printf("\n");
}