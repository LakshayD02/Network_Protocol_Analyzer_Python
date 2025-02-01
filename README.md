# Network Protocol Analyzer Using Python and Scapy 🌐

## Description

This Network Protocol Analyzer captures and logs network traffic in real-time using Python and the Scapy library.  It provides detailed information about network packets, including timestamps, source/destination IP addresses, protocol details (TCP/UDP), and port numbers.  The analyzer automatically selects the best available network interface and logs a configurable number of packets to prevent excessive log file sizes.  This tool is invaluable for network monitoring, analysis, and troubleshooting.

## Features

* **Real-time Packet Sniffing:** Captures network traffic in real-time using Scapy. 📡

* **Automatic Interface Selection:**  Automatically selects the optimal network interface for capturing packets. 💻

* **Detailed Logging:** Logs essential packet details (timestamp, summary, source/destination IPs, protocol, ports) to `network_traffic.log`. 📝

* **Packet Type Identification:** Identifies IP, TCP, and UDP packets and extracts relevant information.  🔎

* **Configurable Logging Limit:** Limits the number of logged packets (default 20) to manage log file size. 🔢

* **Informative Packet Summaries:**  Provides brief summaries of each captured packet. ℹ️

## Technologies Used

* **Python:** The core programming language for the analyzer. 🐍

* **Scapy:** A powerful Python library for network packet manipulation and analysis. 📡

## Ideal For

* **Network Administrators:** Monitoring and analyzing network traffic for troubleshooting and security. 🧑‍💻

* **Security Researchers:**  Investigating network communications and potential threats. 🕵️‍♀️

* **Network Engineers:**  Analyzing network protocols and performance. 👨‍💼

* **Python Developers:** Learning about network programming and packet analysis with Scapy. 🧑‍🎓

## How to Run

1. **Clone the repository:** `git clone <repo url>`

2. **Install Scapy:** `pip install scapy`

3. **Run the program (with appropriate permissions):** `python network_analyzer.py` (or `python3 network_analyzer.py`)  You may need administrator or root privileges to capture network traffic.
