#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <pcap.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/if_ether.h> /* includes net/ethernet.h */


int main(int argc, char *argv[])
{
	// Re-used as error string for pcap
	char errbuf[PCAP_ERRBUF_SIZE]; 

	// Look up devices
	char *dev; // Device for capping
	dev = pcap_lookupdev(errbuf);
	if (dev == NULL) {
		fprintf(stderr, "Couldn't find default device: %s\n", errbuf);
		return(2);
	}
	printf("Device: %s\n", dev);

	// Open device for capping
	pcap_t *handle;
	handle = pcap_open_live(dev, BUFSIZ, 1, 1000, errbuf);
	if (handle == NULL) {
		 fprintf(stderr, "Couldn't open device %s: %s\n", dev, errbuf);
		 return(2);
 	}

 	// Get a packet
 	const u_char *packet;
 	struct pcap_pkthdr packHdr;     /* pcap.h */
 	packet = pcap_next(handle,&packHdr);
 	if(packet == NULL)
    {/* dinna work *sob* */
        printf("Didn't grab packet\n");
        return(2);
    }
	
	// Print packet info	
    printf("Recieved at ..... %s\n",ctime((const time_t*)&packHdr.ts.tv_sec)); 
    printf("Ethernet address length is %d\n",ETHER_ADDR_LEN);
    printf("Grabbed packet of length %d\n",packHdr.len);
    printf("Length of this packets capture:  %d\n",packHdr.caplen);

    

    // Print what type of ethernet packet
    struct ether_header *eptr;  /* net/ethernet.h */
	eptr = (struct ether_header *) packet;
	if (ntohs (eptr->ether_type) == ETHERTYPE_IP)
    {
        printf("Ethernet type hex:%x dec:%d is an IP packet\n",
                ntohs(eptr->ether_type),
                ntohs(eptr->ether_type));
    }else  if (ntohs (eptr->ether_type) == ETHERTYPE_ARP)
    {
        printf("Ethernet type hex:%x dec:%d is an ARP packet\n",
                ntohs(eptr->ether_type),
                ntohs(eptr->ether_type));
    }else {
        printf("Ethernet type %x not IP", ntohs(eptr->ether_type));
        exit(1);
    }

    // Print destination and source addresses
    u_char *ptr; /* printing out hardware header info */
    ptr = eptr->ether_dhost;
    int i = ETHER_ADDR_LEN;
    printf(" Destination Address:  ");
    do{
        printf("%s%x",(i == ETHER_ADDR_LEN) ? " " : ":",*ptr++);
    }while(--i>0);
    printf("\n");

    ptr = eptr->ether_shost;
    i = ETHER_ADDR_LEN;
    printf(" Source Address:  ");
    do{
        printf("%s%x",(i == ETHER_ADDR_LEN) ? " " : ":",*ptr++);
    }while(--i>0);
    printf("\n");


	return(0);
}