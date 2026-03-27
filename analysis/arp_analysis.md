# ARP Analysis

## Protocol Explanation
ARP (Address Resolution Protocol) maps IP addresses to MAC addresses on a local network. It is used to discover the hardware address of devices on the same LAN.

## Wireshark Filter Used
```
arp
```

## Example Packet Breakdown
- **Packet Number:** 41
- **Timestamp:** 2026-03-27 14:09:58.614
- **Source IP:** 192.168.1.1
- **Destination IP:** 192.168.1.10
- **Opcode:** ARP Reply
- **Sender MAC:** 3c:52:82:aa:bb:cc
- **Target MAC:** 88:6b:0f:11:22:33
- **Frame Length:** 60 bytes

## Step-by-Step Packet Behavior
1. A device broadcasts an ARP request: “Who has 192.168.1.10?”
2. The target device responds with its MAC address.
3. Both devices cache the mapping for future traffic.

## Security Relevance
- ARP has no authentication and is vulnerable to spoofing.
- Attackers can send fake ARP replies to redirect traffic (man-in-the-middle risk).

## Evidence to Capture
- **Wireshark Info Column:** `192.168.1.1 is at 3c:52:82:aa:bb:cc`
- **Screenshot:** `screenshots/arp_request_reply.png`
