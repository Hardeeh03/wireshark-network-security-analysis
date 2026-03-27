# TLS Handshake Analysis

## Protocol Explanation
TLS (Transport Layer Security) establishes encrypted sessions for HTTPS and other secure protocols. The handshake negotiates cipher suites, validates certificates, and sets up session keys.

## Wireshark Filter Used
```
tls.handshake
```

## Example Packet Breakdown
- **Packet Number:** 4
- **Timestamp:** 2026-03-27 20:12:16.733
- **Source IP:** 10.136.135.10
- **Destination IP:** 40.126.32.72
- **Source Port:** 1332
- **Destination Port:** 443
- **Handshake Type:** Client Hello
- **Server Name Indication (SNI):** `login.microsoftonline.com`
- **Frame Length:** 529 bytes

## Step-by-Step Packet Behavior
1. Client sends **Client Hello** with supported cipher suites and SNI.
2. Server replies with **Server Hello** and certificate.
3. Key exchange completes and encrypted traffic begins.

## Security Relevance
- TLS protects content but still exposes metadata like SNI and IPs.
- Invalid or self-signed certificates are red flags for potential interception.

## Evidence to Capture
- **Wireshark Info Column:** `Client Hello`
- **Screenshot:** `screenshots/tls_client_hello.png`
- **Screenshot Reference:** `![TLS Client Hello](../screenshots/tls_client_hello.png)`
