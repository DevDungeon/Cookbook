#include <stdio.h>
#include <pcap.h>

int main(int argc, char **argv) {
	char dev[] = "eth0";
	pcap_t *handle;
	char error_buffer[PCAP_ERRBUF_SIZE];
	struct bpf_program filter;
	char filter_exp[] = "port 80";
	bpf_u_int32 subnet_mask, ip;

	if (pcap_lookupnet(dev, &ip, &subnet_mask, error_buffer) == -1) {
		printf("Could not get information for device: %s\n", dev);
		ip = 0;
		subnet_mask = 0;
	}
	handle = pcap_open_live(dev, BUFSIZ, 1, 1000, error_buffer);
	if (handle == NULL) {
		printf("Could not open %s - %s\n", dev, error_buffer);
		return 2;
	}
	if (pcap_compile(handle, &filter, filter_exp, 0, ip) == -1) {
		printf("Bad filter - %s\n", pcap_geterr(handle));
		return 2;
	}
	if (pcap_setfilter(handle, &filter) == -1) {
		printf("Error setting filter - %s\n", pcap_geterr(handle));
		return 2;
	}

	/* pcap_next() or pcap_loop() to get packets from device now */
	/* Only packets over port 80 will be returned. */
	
	return 0;
}