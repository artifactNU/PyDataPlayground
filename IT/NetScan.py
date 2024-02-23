from scapy.all import *

# Function to perform ARP scan to discover active hosts in the network
def network_scan(target):
    # Craft an ARP request packet with the specified target IP range
    arp_request = ARP(pdst=target)
    # Create an Ethernet frame with broadcast destination MAC address
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and ARP request packet
    arp_request_broadcast = broadcast/arp_request
    # Send ARP request packet and capture responses
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    active_hosts = []

    # Extract IP and MAC addresses from the responses
    for element in answered_list:
        host_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        active_hosts.append(host_dict)

    return active_hosts

# Function to perform TCP SYN scan to identify open ports on a target host
def port_scan(target):
    open_ports = []
    # Iterate through common port numbers (1-1024) for scanning
    for port in range(1, 1025):  
        # Craft a TCP SYN packet to the target port
        response = sr1(IP(dst=target)/TCP(dport=port, flags="S"), timeout=1, verbose=False)
        # Check if a response is received and the port is open
        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            open_ports.append(port)
    return open_ports

# Main function to execute the network scanning and port scanning
def main():
    # Prompt user to input target network range
    target_network = input("Enter the target network (e.g., 192.168.1.0/24): ")
    print(f"\nScanning network {target_network}...\n")
    # Perform network scan to identify active hosts
    active_hosts = network_scan(target_network)
    print("Active Hosts:")
    # Display active hosts with their IP and MAC addresses
    for host in active_hosts:
        print(f"IP: {host['ip']}, MAC: {host['mac']}")
    print("\nScanning for open ports...\n")
    # Perform port scan on each active host to identify open ports
    for host in active_hosts:
        open_ports = port_scan(host['ip'])
        if open_ports:
            print(f"Open ports for {host['ip']} : {open_ports}")
        else:
            print(f"No open ports found for {host['ip']}")

# Check if the script is executed directly
if __name__ == "__main__":
    main()
