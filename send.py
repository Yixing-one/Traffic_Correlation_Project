#!/usr/bin/env python3
import argparse
import random
import socket

from debug_hdrs import Debug
from scapy.all import IP, TCP, Ether, get_if_hwaddr, get_if_list, sendp


def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip_addr', type=str, help="The destination IP address to use")
    parser.add_argument('message', type=str, help="The message to include in packet")
    parser.add_argument('--debug', action='store_true', default=False, help='The myTunnel dst_id to use, if unspecified then myTunnel header will not be included in packet')
    args = parser.parse_args()

    addr = socket.gethostbyname(args.ip_addr)
    debug = args.debug
    iface = get_if()

    if debug:
        print("sending on interface {} to dst_id {}".format(iface, str(debug)))
        pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
        pkt = pkt / Debug(debug_field=0) / IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / args.message
    else:
        print("sending on interface {} to IP addr {}".format(iface, str(addr)))
        pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
        pkt = pkt / IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / args.message

    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)


if __name__ == '__main__':
    main()