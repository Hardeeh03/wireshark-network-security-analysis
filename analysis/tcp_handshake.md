# TCP Handshake Analysis

## Protocol Explanation
TCP is a connection-oriented protocol that establishes reliable communication using a three-way handshake: SYN → SYN/ACK → ACK. This occurs before data is exchanged.

## Wireshark Filter Used
```
tcp.flags.syn == 1 and tcp.flags.ack == 0
```
(Use follow-up filters to view the SYN/ACK and ACK packets.)

## Example Packet Breakdown
- **Packet Number:** 1
- **Timestamp:** 2026-03-27 20:12:16.711
- **Source IP:** 10.136.135.10
- **Destination IP:** 40.126.32.72
- **Source Port:** 1332
- **Destination Port:** 443
- **Flags:** SYN
- **Frame Length:** 66 bytes
- **TTL:** 128

## Step-by-Step Packet Behavior
1. Client sends SYN to initiate a connection to port 443 (HTTPS).
2. Server replies with SYN/ACK, acknowledging the request.
3. Client sends ACK, completing the handshake.
4. Encrypted application data begins after the handshake.

## Security Relevance
- Handshakes reveal metadata even when payloads are encrypted.
- Unusual TCP flags or incomplete handshakes can indicate scanning or failed connections.

## Evidence to Capture
- **Wireshark Info Column:** `1332 → 443 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM`
- **Screenshot:** `screenshots/tcp_handshake.png`
- **Screenshot Reference:** `![TCP Handshake](../screenshots/tcp_handshake.png)`
