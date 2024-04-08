import pyshark

def capture_packets(interface, filter_option, bpf_filter, source_ip, destination_ip):
    print(f"Capturing packets on interface {interface}...\n")

    capture = pyshark.LiveCapture(
        interface=interface, display_filter=filter_option, bpf_filter=bpf_filter)

    bpf_filter = f"ip src host {source_ip} and ip dst host {destination_ip}"

    try:
        for packet in capture.sniff_continuously(packet_count=5):
            print("Packet Details:")
            # print(packet)
            print(f"Source IP: {packet.ip.src} | Destination IP: {packet.ip.dst}")
            print(f"Protocol: {packet.transport_layer}")
            print(f"Length: {packet.length} bytes")
            print(f"Timestamp: {packet.sniff_timestamp}")
            print("\n" + "=" * 50 + "\n")

    except KeyboardInterrupt:
        print("Capture interrupted by user.")


def main():
    interface = input("Enter the network interface (e.g., eth0): ")
    filter_option = input(
        "Enter a display filter option (e.g., 'tcp', 'udp', 'icmp', or any valid Wireshark display filter): ")
    bpf_filter = input(
        "Enter a BPF filter (e.g., 'ip', 'tcp port 80', etc.): ")
    
    source_ip = input("Enter the source IP address: ")
    destination_ip = input("Enter the destination IP address: ")

    capture_packets(interface, filter_option, bpf_filter,
                    source_ip, destination_ip)


if __name__ == "__main__":
    main()

# 192.168.20.167
# 192.168.20.107
