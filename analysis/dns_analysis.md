# DNS Analysis

## Protocol Explanation
DNS (Domain Name System) translates human-readable domain names (e.g., `example.com`) into IP addresses. Most DNS traffic uses UDP port 53, which makes queries fast but typically unencrypted.

## Wireshark Filter Used
```
dns
```

## Example Packet Breakdown
**Query**
- **Packet Number:** 3266
- **Timestamp:** 2026-03-27 20:13:25.919
- **Source IP:** 10.136.135.10
- **Destination IP:** 130.43.187.40
- **Protocol/Port:** UDP 53
- **Query:** `A` record for `example.com`
- **Frame Length:** 71 bytes

**Response**
- **Packet Number:** 3267
- **Timestamp:** 2026-03-27 20:13:25.933
- **Source IP:** 130.43.187.40
- **Destination IP:** 10.136.135.10
- **Answer:** `104.18.27.120`, `104.18.26.120`
- **Frame Length:** 103 bytes
- **Response Time:** ~14.4 ms

## Step-by-Step Packet Behavior
1. The client (192.168.1.10) sends a DNS query to the local resolver (192.168.1.1).
2. The resolver responds with the A record for `example.com`.
3. The client uses the resolved IP to initiate a TCP connection to the target host.

## Security Relevance
- DNS queries reveal browsing intent and can be logged or intercepted on the local network.
- Plaintext DNS can be spoofed, leading to malicious redirection.
- Encrypted DNS (DoH/DoT) helps mitigate passive monitoring.

## Evidence to Capture
- **Wireshark Info Column:** `Standard query 0x1229 A example.com` / `Standard query response 0x1229 A example.com A 104.18.27.120`
- **Screenshot:** `screenshots/dns_query_response.png`
- **Screenshot Reference:** `![DNS Query/Response](../screenshots/dns_query_response.png)`
