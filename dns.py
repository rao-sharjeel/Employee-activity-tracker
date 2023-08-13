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
from focusTracker import make_json

dns_urls = []
process_time={}
timestamp = {}
counter = 0
old_time = 0

def process_dns_packet(packet):
    # Get focused apps time
    global process_time
    global timestamp
    global dns_urls
    global old_time
    # t1 = time.time() if old_time == 0 else old_time
    time1 = time.time()
    print(time1)
    print("in the process_dns_packet function")
    try:
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    except:
        current_app = "undefined"
    
    # timestamp[current_app] = time.time()
    
    if current_app not in process_time.keys():
        process_time[current_app] = 0
    
    process_time[current_app] = process_time[current_app] + time.time() - time1 + old_time
    print(process_time)
    time2 = time.time()
    
    # DNS urls tracking
    # if packet.haslayer(DNSQR) and packet.haslayer(IP) and packet[IP].src == '192.168.1.184':
    if packet.haslayer(DNSQR):
        dns_query_name = packet[DNSQR].qname.decode()
        time.sleep(10)
        print("sleeping.......")
        print(dns_query_name)
        if is_valid_url(dns_query_name):
            time.sleep(10)
            dns_urls.append(dns_query_name[0:-1])
            print("valid")
    print(dns_urls)

    old_time = time.time() - time2
    print(old_time)
        
def sniff_dns_traffic():
    print("In sniff_dns_traffic")
    sniff(prn=process_dns_packet, timeout=1)

def track():
    global counter
    global process_time
    global timestamp
    global dns_urls
    print(counter)
    sniff_dns_traffic() # This takes 1 second
    counter += 1
    # print(process_time)
    print(dns_urls)

    if counter == 60:
        print("Sleeping....")
        time.sleep(10)
        print('dns_urls')
        print(dns_urls)
        make_json(process_time, dns_urls)
        process_time={}
        timestamp = {}
        dns_urls = []
        counter = 0
t1 = time.time()

for i in range(10):
    print("i: " + str(i))
    track()
    print("time = " + str(int(time.time() - t1)))