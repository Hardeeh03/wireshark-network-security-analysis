# HTTP vs HTTPS Analysis

## Protocol Explanation
HTTP is plaintext web traffic (typically port 80), while HTTPS uses TLS encryption (typically port 443). HTTPS protects the contents of requests and responses, but metadata like IPs and ports are still visible.

## Wireshark Filter Used
```
http || tls
```

## Example Packet Breakdown
**HTTP (plaintext)**
- **Timestamp:** 2026-03-27 14:10:21.902
- **Source IP:** 192.168.1.10
- **Destination IP:** 93.184.216.34
- **Source Port:** 51601
- **Destination Port:** 80
- **Request:** `GET /` (visible in cleartext)

**HTTPS (encrypted)**
- **Timestamp:** 2026-03-27 14:10:14.233
- **Source IP:** 192.168.1.10
- **Destination IP:** 142.250.74.110
- **Source Port:** 51422
- **Destination Port:** 443
- **Payload:** Encrypted TLS Application Data

## Step-by-Step Packet Behavior
1. HTTP request is sent in cleartext and can be read directly in Wireshark.
2. HTTPS session performs a TLS handshake first.
3. After handshake, encrypted application data is exchanged.

## Security Relevance
- HTTP exposes URLs, cookies, and potentially credentials to anyone sniffing traffic.
- HTTPS protects payloads but still leaks metadata (SNI, IPs, and timing).

## Screenshot Placeholder
- **Screenshot:** HTTP request line visible in packet details and TLS Application Data for HTTPS
