# DNS Analysis

## Protocol Explanation
DNS (Domain Name System) translates human-readable domain names (e.g., `example.com`) into IP addresses. Most DNS traffic uses UDP port 53, which makes queries fast but typically unencrypted.

## Wireshark Filter Used
```
dns
```

## Example Packet Breakdown
- **Timestamp:** 2026-03-27 14:10:12.451
- **Source IP:** 192.168.1.10
- **Destination IP:** 192.168.1.1
- **Protocol/Port:** UDP 53
- **Query:** `A` record for `example.com`
- **Response:** `93.184.216.34`

## Step-by-Step Packet Behavior
1. The client (192.168.1.10) sends a DNS query to the local resolver (192.168.1.1).
2. The resolver responds with the A record for `example.com`.
3. The client uses the resolved IP to initiate a TCP connection to the target host.

## Security Relevance
- DNS queries reveal browsing intent and can be logged or intercepted on the local network.
- Plaintext DNS can be spoofed, leading to malicious redirection.
- Encrypted DNS (DoH/DoT) helps mitigate passive monitoring.

## Screenshot Placeholder
- **Screenshot:** DNS query and response details (expand the packet’s “Domain Name System (query/response)” section)
