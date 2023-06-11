# Sentinel

![Sentinel](https://static.wikia.nocookie.net/robotsupremacy/images/0/08/Squiddy.jpg "Sentinel in action")

This program delves into the depths of your network, tirelessly scanning for arrivals and departures of devices like a vigilant guardian. With the power of mDNS, Sentinel decrypts the elusive identities of each device, unraveling their presence amidst the sea of IP addresses. As the network pulses with life, Sentinel's vigilant whispers deliver real-time notifications waiting for Prometheus pulling data, empowering you to harness the ever-shifting currents of information and fortify your digital realm.

**_Use at your own risk._**

## Usage

### Environment variables

- `DEBUG=true` - more verbose output (default: false)
- `PROMETHEUS_PORT` - prometheus exporter port (default: 65535)
- `SCAN_INTERVAL` - interval between scans in seconds (default: 60)

### With docker

1. Run as docker container connected to host network.

    ```
    docker run -e DEBUG=true -it --network=host radeksh/sentinel
    ```

### Without docker

1. Install system and python dependencies

    ```
    $ sudo apt install nmap avahi-utils
    $ pip install -r sentinel/requirements.txt
    ```

1. Run

    ```
    $ cd sentinel
    $ ./main.py
    ```