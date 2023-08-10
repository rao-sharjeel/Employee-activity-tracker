
from scapy.all import *
import pandas as pd

def process_dns_packet(packet):
    if packet.haslayer(DNSQR) and packet[IP].src == '192.168.1.184':
        dns_query_name = packet[DNSQR].qname.decode()
        # url_split = dns_query_name.split('.')[0:-1]
        # url_data.append([dns_query_name[0:-1], len(url_split), len(url_split) <= 3, has_api_word(url_split), hidden_api_word(url_split), has_ad(url_split), has_hiphen(url_split), has_domain_format(url_split), has_single_char(url_split)])
        if is_valid_url(dns_query_name):
            return dns_query_name[0:-1]
        # print(packet.summary())
        print(len(url_data))

def sniff_dns_traffic():
    # Filter DNS traffic on port 53
    sniff(filter="udp port 53", prn=process_dns_packet, stop_filter=lambda x: len(url_data) >= 500)

if __name__ == "__main__":
    sniff_dns_traffic()
    df = pd.DataFrame(url_data, columns=["DNS Query Name", "URL Components Count", "Is <=3", "Has API Keyword", "Has Api Substring", "Has Ad substring", "Has hiphen", "Has URL format", "Has Single Char"])
    # df.to_csv('dns_data_new.csv')
    # print(df.head(20))


