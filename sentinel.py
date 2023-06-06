#!/usr/bin/env python3

import asyncio
import time, subprocess
import netifaces, ipaddress
from prometheus_client import start_http_server, Gauge

SCAN_INTERVAL = 60

connected_devices = []
device_gauge = Gauge('device_connected', 'Network devices state ', ['ip', 'hostname'])

async def resolve_device_hostname(ip):
    try:
        process = await asyncio.create_subprocess_exec("avahi-resolve", "-a", ip, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        exit("Package avahi-resolve not found. Please install avahi-utils.")
    output, errors = await process.communicate()
    return {"ip": ip, "hostname": output.decode("utf-8").split("\t")[1].strip("\n").split(".")[0] if output else None}


async def get_network_devices_states(network):
    global connected_devices
    current_devices_ips = []

    process = await asyncio.create_subprocess_exec("nmap", "-sn", network, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = await process.communicate()
    if output:
        output = output.decode("utf-8")
        for line in output.split("\n"):
            if "Nmap scan report for" in line:
                ip = line.split(" ")[-1].strip("()")
                current_devices_ips.append(ip)

    connected_devices_ips = [device["ip"] for device in connected_devices]
    left_devices_ips = [ip for ip in connected_devices_ips if ip not in current_devices_ips]
    new_seen_ips = [ip for ip in current_devices_ips if ip not in connected_devices_ips]
    tasks = [asyncio.create_task(resolve_device_hostname(ip)) for ip in new_seen_ips]

    joined_devices = await asyncio.gather(*tasks)
    connected_devices.extend(joined_devices)

    left_devices = [device for device in connected_devices if device["ip"] in left_devices_ips]
    connected_devices = [device for device in connected_devices if device["ip"] not in left_devices_ips]

    return {"joined": joined_devices, "left": left_devices}


def get_default_gateway():
    gateways = netifaces.gateways()
    interface = gateways['default'][netifaces.AF_INET][1]
    interfaces = netifaces.ifaddresses(interface)
    network_address = interfaces[netifaces.AF_INET][0]['addr']
    netmask = interfaces[netifaces.AF_INET][0]['netmask']
    network = ipaddress.IPv4Network(f"{network_address}/{netmask}", strict=False)
    return str(network)


def update_device_gauge(devices_status):
    for device in devices_status["joined"]:
        device_gauge.labels(**device).set(1)
    for device in devices_status["left"]:
        device_gauge.labels(**device).set(0)


if __name__ == "__main__":
    start_http_server(65535)
    network = get_default_gateway()
    loop = asyncio.get_event_loop()

    while True:
        devices_status = loop.run_until_complete(get_network_devices_states(network))
        #print(devices_status)
        update_device_gauge(devices_status)
        time.sleep(SCAN_INTERVAL)
