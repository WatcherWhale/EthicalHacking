#!/usr/bin/env python3

# Just the tool

import argparse

from scapy.layers.l2 import Ether, ARP, srp
from scapy.layers.inet import IP, TCP, sr, TCP_client, ICMP, sr1
from scapy.sendrecv import sniff, wrpcap
from scapy.layers.http import HTTP, HTTPRequest

import threading
import time

import sys

def main():
    args = parse_args()

    if args.attack == "arp_discover":
        arp_discover(args.target)
    elif args.attack == "port":
        port_scan(args.target)
    elif args.attack == "os":
        host(args.target)
    elif args.attack == "pcap":
        pcap(args.target)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Netack",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('attack')
    parser.add_argument('-t', '--target')
    parser.add_argument('-v', '--verbose')

    return parser.parse_args()

def arp_discover(target):
    print("Discover " + target)
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target), timeout=2)
    ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

def port_scan(target):
    ans, unans = sr(IP(dst=target)/TCP(dport=(1,1024), flags="S"))
    ans.nsummary(lambda s,r: r.sprintf("%TCP.sport%"), lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)))

def host(target):
    res = sr1(IP(dst=target)/ICMP(), timeout=5)

    ttl = res.getlayer(IP).ttl

    if ttl == 64:
        print("Unix")
    elif ttl == 128:
        print("Windows")
    elif ttl == 255:
        print("Cisco Router")

def pcap(target):
    th = threading.Thread(target=pcap_send, args=(target,))
    th.start()
    pkts = sniff()
    wrpcap("sniff.pcap", pkts)
    th.join()

def pcap_send(target: str):
    time.sleep(2)
    req = HTTP()/HTTPRequest(
        Accept_Encoding=b'gzip, deflate',
        Cache_Control=b'no-cache',
        Connection=b'keep-alive',
        Host=target.encode(),
        Pragma=b'no-cache'
    )

    a = TCP_client.tcplink(HTTP, target, 80)
    answer = a.sr1(req)
    a.close()

if __name__ == "__main__":
    main()
