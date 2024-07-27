# Network Protocol Analyzer Using Python and Scapy

The Network Protocol Analyzer is a tool designed to capture and log network traffic in real-time. Built on Python using the Scapy library, this analyzer provides insights into various network packets traversing the interface, allowing for effective monitoring and analysis of network communications.

# Key Features:

- Real-time Packet Sniffing:

The analyzer utilizes Scapy's powerful packet manipulation capabilities to sniff network traffic without the need for specifying an interface. It automatically selects the best available network interface for capturing packets. Packets are processed as they are captured, enabling immediate logging and analysis of network activities.

- Detailed Logging:

The system logs essential details of each captured packet to a log file named network_traffic.log. The logs include timestamps, packet summaries, source and destination IP addresses, and protocol details (TCP/UDP).
This logging mechanism enables users to review captured traffic for potential analysis and troubleshooting.

- Packet Type Identification:

The analyzer identifies various types of packets by checking for specific layers, such as IP, TCP, and UDP. Upon detecting an IP packet, it captures the source and destination IP addresses, as well as the protocol used. For TCP and UDP packets, the source and destination port numbers are also recorded, providing a comprehensive overview of the traffic being monitored.

- Configurable Logging Limit:

The analyzer is designed to log a limited number of packets (set to 20 in this implementation) to avoid excessive log file sizes and to focus on a manageable subset of traffic. The logging limit can be easily adjusted by modifying the max_packets variable within the code.
