from scapy.all import *
from dns_helpers import is_valid_url
i = 0
def process_dns_packet(packet):
    global i
    print(i)
    i += 1
    if packet.haslayer(DNSQR):
        # Extract the DNS query name from the DNS Question Record (DNSQR)
        dns_query_name = packet[DNSQR].qname.decode()
        print(f"DNS Query: {dns_query_name}")
        print("is valid" + str(is_valid_url(dns_query_name)))

def sniff_dns_traffic():
    # Filter DNS traffic on port 53
    sniff(filter="udp port 53", prn=process_dns_packet)

sniff_dns_traffic()
