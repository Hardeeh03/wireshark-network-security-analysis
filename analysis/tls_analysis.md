# TLS Handshake Analysis

## Protocol Explanation
TLS (Transport Layer Security) establishes encrypted sessions for HTTPS and other secure protocols. The handshake negotiates cipher suites, validates certificates, and sets up session keys.

## Wireshark Filter Used
```
tls.handshake
```

## Example Packet Breakdown
- **Timestamp:** 2026-03-27 14:10:13.115
- **Source IP:** 192.168.1.10
- **Destination IP:** 142.250.74.110
- **Source Port:** 51422
- **Destination Port:** 443
- **Handshake Type:** Client Hello
- **Server Name Indication (SNI):** `www.google.com`

## Step-by-Step Packet Behavior
1. Client sends **Client Hello** with supported cipher suites and SNI.
2. Server replies with **Server Hello** and certificate.
3. Key exchange completes and encrypted traffic begins.

## Security Relevance
- TLS protects content but still exposes metadata like SNI and IPs.
- Invalid or self-signed certificates are red flags for potential interception.

## Screenshot Placeholder
- **Screenshot:** TLS Client Hello with SNI field highlighted
