# NetSentinel

![NetSentinel](https://static.wikia.nocookie.net/robotsupremacy/images/0/08/Squiddy.jpg "NetSentinel in action")

This program delves into the depths of your network, tirelessly scanning for arrivals and departures of devices like a vigilant guardian. With the power of mDNS, NetSentinel decrypts the elusive identities of each device, unraveling their presence amidst the sea of IP addresses. As the network pulses with life, NetSentinel's vigilant whispers deliver real-time notifications waiting for Prometheus pulling data, empowering you to harness the ever-shifting currents of information and fortify your digital realm.

**Created one quiet evening for fun. _Use at your own risk._**

## Usage

1. Install dependencies

    ```
    $ sudo apt install nmap avahi-utils
    $ pip install -r requirements.txt
    ```
1. Run
    ```
    $ ./sentinel.py
    ```
