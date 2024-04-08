import pyshark
from scapy.all import *


def capture_packets(interface, filter_option):
    print(f"Capturing packets on interface {interface}...\n")
    pc = int(input("Enter Packet count: "))
    capture = pyshark.LiveCapture(
        interface=interface, display_filter=filter_option)

    try:
        for packet in capture.sniff_continuously(packet_count=pc):
            print("Packet Details:")
            print(packet)
            print("\n__________________________________________________________\n")

    except KeyboardInterrupt:
        print("Capture interrupted.")


def main():
    interface = input("Enter the network interface (eg: Wi-Fi): ")

    filter_option = input(
        "Enter a filter option (eg: 'tcp', 'icmp'): ")

    capture_packets(interface, filter_option)


if __name__ == "__main__":
    main()
