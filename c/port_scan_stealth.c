// Compile with
// gcc synscan.c -lpcap
#include <stdio.h>
#include <pcap.h>
#include <memory.h>
#include <stdint.h>




void print_usage() {
    printf("Usage:\n");
    printf("  synscan <host> <port> <interface>\n");
    printf("Example usage:\n");
    printf("  synscan www.devdungeon.com 22 eth0\n");
    printf("  synscan 8.8.8.8 53 ens22\n");
}


struct ip_header {
    // src ip
    // dest ip
    // version
//    __u8 	tos
//    __u16 	tot_len
//    __u16 	id
//    __u16 	frag_off
//    __u8 	ttl
//    __u8 	protocol
//    __u16 	check
//    __u32 	saddr
//    __u32 	daddr
};

struct tcp_header {
    uint16_t src_port;  /* source port */
    uint16_t dst_port;  /* destination port */
    uint32_t seq;   /* sequence number */
    uint32_t ack;   /* acknowledgement number */

#if BYTE_ORDER == LITTLE_ENDIAN
    u_int th_x2:4,  /* (unused) */
            th_off:4;  /* data offset */
#endif
#if BYTE_ORDER == BIG_ENDIAN
    u_int th_off:4,  /* data offset */
  th_x2:4;  /* (unused) */
#endif
    u_char flags;
#define TH_FIN 0x01
#define TH_SYN 0x02
#define TH_RST 0x04
#define TH_PUSH 0x08
#define TH_ACK 0x10
#define TH_URG 0x20
#define TH_ECE 0x40
#define TH_CWR 0x80
#define TH_FLAGS (TH_FIN|TH_SYN|TH_RST|TH_ACK|TH_URG|TH_ECE|TH_CWR)

    u_short win;   /* window */
    u_short sum;   /* checksum */
    u_short urp;   /* urgent pointer */
};


void send_syn_packet(pcap_t *handle, char *host, char *port) {
    printf("Sending SYN packet to %s:%s\n", host, port);
    struct tcp_header out_packet;
    // Set all flags on the tcp packet
    out_packet.ack = 0;
    out_packet.seq = 0;
    out_packet.flags = 2; // SYN only set
    // TODO combine the IP header + TCP header
    // TODO Set other properties, like checksum?
    pcap_sendpacket(handle, (u_char*)&out_packet, sizeof(out_packet));
}

void synscan(char *host, char *port, char *interface) {
    char error_buffer[PCAP_ERRBUF_SIZE];
    struct pcap_pkthdr header;

    pcap_t *handle = pcap_open_live(interface, 4096, 10000, 3000, error_buffer);
    printf("Opened device %s for reading.\n", interface);

    // void kick_off_synack_listener(host, port, interface, handle);
    { // TODO do this capturing in a separate thread
        struct bpf_program filter;
        char filter_string[] = "tcp[13] = 18 and src host "; // TODO ANd? sequence 0 and ack number 1? and dst port will equal original src port
        char final_filter_string[strlen(filter_string) + strlen(host) + 1];
        strcpy(final_filter_string, filter_string);
        strcat(filter_string, host);

        bpf_u_int32 ip = 0;
        pcap_compile(handle, &filter, filter_string, 0, ip);
        pcap_setfilter(handle, &filter);
        printf("Set filter: %s\n", filter_string);

        const u_char *packet = pcap_next(handle, &header);
        if (packet == NULL) {
            printf("No packet received.\n");
            return;
        }
        printf("Captured packet length: %d\n", header.caplen);

        // TODO Lock and update the mutual object and signal done
    }


    send_syn_packet(handle, host, port);


    // TODO While the mutual object is not updated with a response & timeout not reached
        // TODO checking the mutual object// wait for lock?
        // TODO If it did receive synack then send reset

}

int main(int argc, char **argv)  {

    // If not enough arguments provided, printusage and quit
    if (argc < 4) {
        printf("Not enough arguments provided.\n");
        print_usage();
        return 1;
    }

    char *host = argv[1];
    char *port = argv[2];
    char *interface = argv[3];
    printf("Scanning %s:%s using interface %s.\n", host, port, interface);

    // DO the scan
    synscan(host, port, interface);


    return 0;
}
