import os  # Import untuk modul os
import socket
import ipaddress

# Fungsi untuk mengimbas port tertentu pada IP
def scan_specific_ports(ip, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            continue
    return open_ports

# Fungsi untuk mengimbas semua port dari 1 hingga 1024
def scan_ports(ip):
    return scan_specific_ports(ip, range(1, 1025))

# Fungsi untuk validasi IP Address
def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Fungsi untuk ujian ping
def ping_ip(ip):
    response = os.system(f"ping -c 1 {ip}")
    return response == 0

# Fungsi untuk memaparkan banner
def print_banner():
    banner = """
##::::'##::::'###::::'##::: ##::'######::::::'########:'##::::'##::::'###::::'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:'##... ##:::::... ##..:: ##:::: ##:::'## ##::: ##:::: ##:
 ##:::: ##::'##:. ##:: ####: ##: ##:::..::::::::: ##:::: ##:::: ##::'##:. ##:: ##:::: ##:
 #########:'##:::. ##: ## ## ##: ##::'####::::::: ##:::: ##:::: ##:'##:::. ##: #########:
 ##.... ##: #########: ##. ####: ##::: ##:::::::: ##:::: ##:::: ##: #########: ##.... ##:
 ##:::: ##: ##.... ##: ##:. ###: ##::: ##:::::::: ##:::: ##:::: ##: ##.... ##: ##:::: ##:
 ##:::: ##: ##:::: ##: ##::. ##:. ######::::::::: ##::::. #######:: ##:::: ##: ##:::: ##:
..:::::..::..:::::..::..::::..:::......::::::::::..::::::.......:::..:::::..::..:::::..::
    """
    print(banner)

# Fungsi utama untuk imbasan
def main():
    print_banner()  # Paparkan banner

    ip_list = input("Masukkan senarai IP (pisahkan dengan koma): ").split(',')
    for ip in ip_list:
        ip = ip.strip()
        if validate_ip(ip):
            print(f"\nImbasan untuk IP: {ip}")
            print("-" * 40)
            
            # Ujian ping
            if ping_ip(ip):
                print(f"{ip} aktif, memulakan imbasan port...")
                # Pilih untuk imbasan port tertentu atau semua
                choice = input("Imbas semua port (1-1024) atau pilih port tertentu? (a/t): ").lower()
                if choice == 'a':
                    open_ports = scan_ports(ip)
                else:
                    ports = list(map(int, input("Masukkan port (pisahkan dengan koma): ").split(',')))
                    open_ports = scan_specific_ports(ip, ports)
                
                if open_ports:
                    print(f"\nPort yang terbuka untuk {ip}:")
                    print("-" * 40)
                    for port in open_ports:
                        print(f"Port {port}: Terbuka")
                else:
                    print("Tiada port terbuka ditemui.")
            else:
                print(f"{ip} tidak aktif atau tidak dapat dihubungi.")
            print("-" * 40)  # Penutup untuk setiap IP
        else:
            print(f"{ip} adalah IP address yang tidak sah.")

if __name__ == "__main__":
    main()
