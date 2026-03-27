# DNS Analysis

## Protocol Explanation
DNS (Domain Name System) translates human-readable domain names (e.g., `example.com`) into IP addresses. Most DNS traffic uses UDP port 53, which makes queries fast but typically unencrypted.

## Wireshark Filter Used
```
dns
```

## Example Packet Breakdown
- **Packet Number:** 143
- **Timestamp:** 2026-03-27 14:10:12.451
- **Source IP:** 192.168.1.10
- **Destination IP:** 192.168.1.1
- **Protocol/Port:** UDP 53
- **Query:** `A` record for `example.com`
- **Response:** `93.184.216.34`
- **Frame Length:** 74 bytes
- **Response Time:** 28 ms

## Step-by-Step Packet Behavior
1. The client (192.168.1.10) sends a DNS query to the local resolver (192.168.1.1).
2. The resolver responds with the A record for `example.com`.
3. The client uses the resolved IP to initiate a TCP connection to the target host.

## Security Relevance
- DNS queries reveal browsing intent and can be logged or intercepted on the local network.
- Plaintext DNS can be spoofed, leading to malicious redirection.
- Encrypted DNS (DoH/DoT) helps mitigate passive monitoring.

## Evidence to Capture
- **Wireshark Info Column:** `Standard query 0x4c9f A example.com` / `Standard query response 0x4c9f A 93.184.216.34`
- **Screenshot:** `screenshots/dns_query_response.png`
