import sys
import socket
from scapy.all import *
import requests

def scan_ports(ip, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        try:
            syn_packet = IP(dst=ip)/TCP(dport=port, flags="S")
            response = sr1(syn_packet, timeout=1, verbose=0)
            if response and response.haslayer(TCP) and response[TCP].flags == 18:  # SYN-ACK flag
                open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {str(e)}")
    return open_ports

def get_geolocation(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            return {
                'country': data.get('country', 'N/A'),
                'regionName': data.get('regionName', 'N/A'),
                'city': data.get('city', 'N/A'),
                'lat': data.get('lat', 'N/A'),
                'lon': data.get('lon', 'N/A'),
                'isp': data.get('isp', 'N/A')
            }
        else:
            return None
    except Exception as e:
        print(f"Error retrieving geolocation data: {str(e)}")
        return None

def scan_ip(ip, port_range=(20, 1024)):
    print(f"\nScanning IP: {ip}")
    
    # Port scanning
    open_ports = scan_ports(ip, port_range)
    
    # Geolocation lookup
    geolocation = get_geolocation(ip)
    
    # Display results
    print(f"Open Ports: {open_ports}")
    if geolocation:
        print(f"Geolocation: {geolocation['city']}, {geolocation['regionName']}, {geolocation['country']}")
        print(f"Coordinates: {geolocation['lat']}, {geolocation['lon']}")
        print(f"ISP: {geolocation['isp']}")
    else:
        print("Failed to retrieve geolocation data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ip_scan_geo.py <target_ip>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    scan_ip(target_ip)
