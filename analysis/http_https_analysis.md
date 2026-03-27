# HTTP vs HTTPS Analysis

## Protocol Explanation
HTTP is plaintext web traffic (typically port 80), while HTTPS uses TLS encryption (typically port 443). HTTPS protects the contents of requests and responses, but metadata like IPs and ports are still visible.

## Wireshark Filter Used
```
http || tls
```

## Example Packet Breakdown
**HTTP (plaintext)**
- **Packet Number:** 4578
- **Timestamp:** 2026-03-27 20:13:34.804
- **Source IP:** 10.136.135.10
- **Destination IP:** 2.19.252.157
- **Source Port:** 30282
- **Destination Port:** 80
- **Request:** `GET /ncsi.txt` (visible in cleartext)
- **Frame Length:** 178 bytes

**HTTPS (encrypted)**
- **Packet Number:** 10
- **Timestamp:** 2026-03-27 20:12:16.767
- **Source IP:** 10.136.135.10
- **Destination IP:** 40.126.32.72
- **Source Port:** 1332
- **Destination Port:** 443
- **Payload:** Encrypted TLS Application Data
- **Frame Length:** 134 bytes

## Step-by-Step Packet Behavior
1. HTTP request is sent in cleartext and can be read directly in Wireshark.
2. HTTPS session performs a TLS handshake first.
3. After handshake, encrypted application data is exchanged.

## Security Relevance
- HTTP exposes URLs, cookies, and potentially credentials to anyone sniffing traffic.
- HTTPS protects payloads but still leaks metadata (SNI, IPs, and timing).

## Evidence to Capture
- **Wireshark Info Column (HTTP):** `GET /ncsi.txt HTTP/1.1`
- **Wireshark Info Column (TLS):** `Change Cipher Spec, Application Data`
- **Screenshots:** `screenshots/http_request.png`, `screenshots/https_tls_appdata.png`
- **Screenshot References:** `![HTTP Request](../screenshots/http_request.png)` and `![HTTPS TLS Application Data](../screenshots/https_tls_appdata.png)`
