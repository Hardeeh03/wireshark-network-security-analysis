# Wireshark Packet Analysis Lab

## Project Overview
This project documents a hands-on Wireshark packet analysis lab focused on understanding how common network protocols behave and what security insights can be learned from real traffic. The lab captures a short, controlled burst of local traffic and breaks it down into DNS, TCP, HTTP/HTTPS, ARP, ICMP, and TLS behaviors using practical filters and packet walkthroughs.

## Objectives
- Capture a short sample of local network traffic in a safe, controlled session.
- Identify and interpret key protocol behaviors in Wireshark.
- Document packet details with realistic examples and security context.
- Build a portfolio-ready writeup demonstrating foundational network analysis skills.

## Tools Used
- **Wireshark** (GUI packet capture and analysis)
- **tshark** (optional CLI capture script)

## Step-by-Step Setup
### Windows
1. Download and install Wireshark from the official site.
2. During installation, allow the Npcap driver to be installed.
3. Launch Wireshark as Administrator for full capture permissions.

### macOS
1. Install Wireshark via the official DMG or Homebrew.
2. Allow packet capture permissions when prompted.
3. Run Wireshark and select your active interface (usually Wi-Fi).

### Linux
1. Install Wireshark using your distro package manager.
2. Add your user to the `wireshark` group (or run with sudo).
3. Start Wireshark and select your active interface.

## Capture Methodology
- Capture window: **3–5 minutes**
- Activities performed:
  - Opened a browser and visited 2–3 HTTPS websites
  - Ran a DNS lookup to a known domain
  - Pinged a public IP
- Goal: Generate enough traffic to observe protocol behavior without capturing unrelated data

## Analysis Workflow
1. Start capture on the active interface for 3–5 minutes.
2. Stop capture and save as `captures/sample_capture.pcapng`.
3. Apply protocol filters one at a time.
4. For each protocol:
   - Identify an example packet
   - Record packet number, timestamps, IPs, ports, and key fields
   - Summarize behavior and security relevance
5. Export or capture screenshots for key packet details.

## Suggested Filters
- DNS: `dns`
- TCP handshake (SYN): `tcp.flags.syn == 1 and tcp.flags.ack == 0`
- HTTP: `http`
- HTTPS/TLS: `tls` or `tcp.port == 443`
- ARP: `arp`
- ICMP: `icmp`
- TLS handshake: `tls.handshake`

## Protocols Analyzed
- DNS
- TCP (3-way handshake)
- HTTP vs HTTPS
- ARP
- ICMP
- TLS handshake

## Analysis Files
- `analysis/dns_analysis.md`
- `analysis/tcp_handshake.md`
- `analysis/http_https_analysis.md`
- `analysis/arp_analysis.md`
- `analysis/icmp_analysis.md`
- `analysis/tls_analysis.md`

## Optional tshark Capture Script
An optional script is provided in `scripts/capture_tshark.py` for CLI-based captures.

**Example usage:**
```
python scripts/capture_tshark.py -i 1 -d 300
```

**Notes:**
- List interfaces with `tshark -D`
- Output files are stored in `captures/` by default

## Evidence Artifacts
- Screenshots: add images to `screenshots/` and link them from each analysis file.
- Capture: add a sanitized sample to `captures/` (remove personal identifiers).

## Key Findings
- Most web traffic is encrypted (HTTPS/TLS), but DNS remains visible unless encrypted DNS is used.
- TCP handshakes are consistent and reveal connection setup even when payloads are encrypted.
- ARP traffic can expose local device discovery and is vulnerable to spoofing.
- ICMP traffic is simple but useful for diagnostics and can be abused for reconnaissance.

## Security Insights
- **HTTPS encryption importance:** Protects content from passive sniffing.
- **Risks of HTTP:** Credentials and content can be read in plaintext on unencrypted sites.
- **ARP spoofing concept:** Attackers on the LAN can impersonate devices to intercept traffic.
- **Packet sniffing risks:** Anyone with local access can observe metadata and unencrypted traffic.

## Learning Outcomes
- Developed practical Wireshark filtering and inspection skills.
- Built confidence interpreting packet structures and protocol flows.
- Learned to document traffic in a clear, portfolio-ready format.

## Future Improvements
- Analyze DHCP and IPv6 traffic
- Compare encrypted DNS (DoH/DoT) vs plaintext DNS
- Add traffic from a virtual lab environment for richer protocol coverage

---

For protocol-specific breakdowns, see the files in `analysis/`.
