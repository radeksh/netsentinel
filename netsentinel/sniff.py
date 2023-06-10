#!/usr/bin/env python3

import time
import os
from contextlib import contextmanager
from scapy.all import Dot11Beacon, Dot11Elt, sniff


@contextmanager
def monitor_mode(interface):
    """ Set interface to monitor mode.
    """
    os.system(f"sudo iw {interface} set monitor control")
    try:
        yield
    finally:
        os.system(f"sudo iw {interface} set type managed")


def handle_beacon(pkt):
    if pkt.haslayer(Dot11Beacon):
        print({
            "SSID": pkt.info.decode(),
            "BSSID:": pkt.addr3,
            "Channel": ord(pkt[Dot11Elt:3].info),
            "Signal": pkt.dBm_AntSignal,
        })


def sniff_ap_beacons(interface):
    """ Sniff AP beacons on all 2.4GHz channels.
        In most cases you should see all APs in your area in one minute.
    """
    with monitor_mode(interface):
        for channel in range(1, 15):
            os.system(f"sudo iw dev {interface} set channel {channel}")
            sniff(iface=interface, timeout=4, prn=handle_beacon, filter="type mgt and subtype beacon")
