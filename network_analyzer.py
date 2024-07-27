from scapy.all import *
import logging

# Set up logging to log packet details to a file
logging.basicConfig(filename='network_traffic.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Global variable to keep track of the number of logged packets
packet_count = 0

def packet_callback(packet):
    global packet_count
    max_packets = 20  # Set the logging limit here (10-20 packets)

    # Log the packet summary
    if packet_count < max_packets:
        logging.info(packet.summary())
        
        # Capture more details based on the packet type
        if packet.haslayer(IP):
            ip_layer = packet[IP]
            logging.info(f"Source IP: {ip_layer.src}, Destination IP: {ip_layer.dst}, Protocol: {ip_layer.proto}")

        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            logging.info(f"Source Port: {tcp_layer.sport}, Destination Port: {tcp_layer.dport}")

        if packet.haslayer(UDP):
            udp_layer = packet[UDP]
            logging.info(f"Source Port: {udp_layer.sport}, Destination Port: {udp_layer.dport}")

        packet_count += 1  # Increment the packet count

def main():
    # Start sniffing the network
    print("Starting packet capture. Press Ctrl+C to stop.")
    try:
        # Start sniffing without specifying the interface; Scapy will automatically choose the best one
        sniff(prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("Packet capture stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
