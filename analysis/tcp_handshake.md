# TCP Handshake Analysis

## Protocol Explanation
TCP is a connection-oriented protocol that establishes reliable communication using a three-way handshake: SYN → SYN/ACK → ACK. This occurs before data is exchanged.

## Wireshark Filter Used
```
tcp.flags.syn == 1 and tcp.flags.ack == 0
```
(Use follow-up filters to view the SYN/ACK and ACK packets.)

## Example Packet Breakdown
- **Timestamp:** 2026-03-27 14:10:13.008
- **Source IP:** 192.168.1.10
- **Destination IP:** 142.250.74.110
- **Source Port:** 51422
- **Destination Port:** 443
- **Flags:** SYN

## Step-by-Step Packet Behavior
1. Client sends SYN to initiate a connection to port 443 (HTTPS).
2. Server replies with SYN/ACK, acknowledging the request.
3. Client sends ACK, completing the handshake.
4. Encrypted application data begins after the handshake.

## Security Relevance
- Handshakes reveal metadata even when payloads are encrypted.
- Unusual TCP flags or incomplete handshakes can indicate scanning or failed connections.

## Screenshot Placeholder
- **Screenshot:** TCP handshake packets highlighted in packet list with flag details visible
