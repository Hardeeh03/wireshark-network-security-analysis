# ARP Analysis

## Protocol Explanation
ARP (Address Resolution Protocol) maps IP addresses to MAC addresses on a local network. It is used to discover the hardware address of devices on the same LAN.

## Wireshark Filter Used
```
arp
```

## Example Packet Breakdown
**Request**
- **Packet Number:** 117
- **Timestamp:** 2026-03-27 20:12:27.571
- **Source IP:** 10.136.135.1
- **Destination IP:** 10.136.135.10
- **Opcode:** ARP Request (1)
- **Sender MAC:** 2c:c8:1b:99:11:a5
- **Target MAC:** 00:00:00:00:00:00
- **Frame Length:** 60 bytes

**Reply**
- **Packet Number:** 118
- **Timestamp:** 2026-03-27 20:12:27.571
- **Source IP:** 10.136.135.10
- **Destination IP:** 10.136.135.1
- **Opcode:** ARP Reply (2)
- **Sender MAC:** 38:7a:0e:d7:73:0f
- **Target MAC:** 2c:c8:1b:99:11:a5
- **Frame Length:** 42 bytes

## Step-by-Step Packet Behavior
1. A device broadcasts an ARP request: “Who has 10.136.135.10?”
2. The target device responds with its MAC address.
3. Both devices cache the mapping for future traffic.

## Security Relevance
- ARP has no authentication and is vulnerable to spoofing.
- Attackers can send fake ARP replies to redirect traffic (man-in-the-middle risk).

## Evidence to Capture
- **Wireshark Info Column:** `Who has 10.136.135.10? Tell 10.136.135.1` and `10.136.135.10 is at 38:7a:0e:d7:73:0f`
- **Screenshot:** `screenshots/arp_request_reply.png`
- **Screenshot Reference:** `![ARP Request/Reply](../screenshots/arp_request_reply.png)`
