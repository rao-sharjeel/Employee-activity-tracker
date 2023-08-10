from scapy.all import *
import pandas as pd
from win32gui import GetForegroundWindow
import psutil
import time
import win32process
from getRunningApps import get_active_window_title, get_running_processes
from takeScreenshot import take_screenshot
import json
from datetime import datetime
from dns_helpers import is_valid_url

final = ""
api_keywords = ["api","beacons", "static", "sdk", "amazonaws", "aws", "client", "cdn", "rtb", "pbs", "fastlane", "cloudfront", "webapi", "service", "endpoint", "font", "fonts", "content", "json", "xml", "rpc", "rest", "graphql", "soap", "v1", "v2", "v3", "v4", "v5", "data", "get", "post", "put", "delete", "patch", "call", "method", "action", "query", "resource", "fetch", "retrieve", "send", "receive", "create", "update", "delete", 'googleapis']
url_data = []
process_time={}
timestamp = {}

def process_dns_packet(packet):
    # Get focused apps time
    try:
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    except:
        current_app = "undefined"
    timestamp[current_app] = int(time.time())
    
    if current_app not in process_time.keys():
        process_time[current_app] = 0
    process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
    counter += 1
    print(process_time)

    if packet.haslayer(DNSQR) and packet[IP].src == '192.168.1.184':
        dns_query_name = packet[DNSQR].qname.decode()
        if is_valid_url(dns_query_name):
            return dns_query_name[0:-1]
        
def sniff_dns_traffic():
    sniff(filter="udp port 53", prn=process_dns_packet, timeout=1)



