// If using qt creator, add these
// to the project file in Windows
// 
//# Pcap specific build stuff for Windows
//INCLUDEPATH += C:/WpdPack/Include
//LIBS += C:/WpdPack/Lib/wpcap.lib
//LIBS += C:/WpdPack/Lib/Packet.lib
//CONFIG += no_lflags_merge
//
//# Fixes the missing inet_to_ntoa
//LIBS += -lws2_32



#define HAVE_REMOTE
#include <winsock2.h>
#include "pcap.h"

/* prototype of the packet handler */
void packet_handler(u_char *param, const struct pcap_pkthdr *header, const u_char *pkt_data);

int main()
{
pcap_if_t *alldevs;
pcap_if_t *d;
int inum;
int i=0;
pcap_t *adhandle;
char errbuf[PCAP_ERRBUF_SIZE];

    /* Retrieve the device list on the local machine */
    if (pcap_findalldevs_ex(PCAP_SRC_IF_STRING, NULL, &alldevs, errbuf) == -1)
    {
        fprintf(stderr,"Error in pcap_findalldevs: %s\n", errbuf);
        exit(1);
    }

    /* Print the list */
    for(d=alldevs; d; d=d->next)
    {
        printf("%d. %s", ++i, d->name);
        if (d->description)
            printf(" (%s)\n", d->description);
        else
            printf(" (No description available)\n");
    }

    if(i==0)
    {
        printf("\nNo interfaces found! Make sure WinPcap is installed.\n");
        return -1;
    }
}
