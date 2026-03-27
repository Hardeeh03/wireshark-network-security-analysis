# ICMP Analysis

## Protocol Explanation
ICMP is used for network diagnostics and error reporting. The most common use is the `ping` command, which sends Echo Request and receives Echo Reply packets.

## Wireshark Filter Used
```
icmp
```

## Example Packet Breakdown
- **Packet Number:** 301
- **Timestamp:** 2026-03-27 14:10:30.487
- **Source IP:** 192.168.1.10
- **Destination IP:** 8.8.8.8
- **Type:** 8 (Echo Request)
- **Identifier/Sequence:** id=0x0042, seq=1
- **Frame Length:** 74 bytes
- **Round-Trip Time:** 21 ms

## Step-by-Step Packet Behavior
1. The client sends an Echo Request to the target IP.
2. The target responds with an Echo Reply (Type 0).
3. Round-trip time can be measured from timestamps.

## Security Relevance
- ICMP can be used by attackers for reconnaissance (host discovery).
- Some networks restrict ICMP to reduce visibility.

## Evidence to Capture
- **Wireshark Info Column:** `Echo (ping) request` / `Echo (ping) reply`
- **Screenshot:** `screenshots/icmp_echo.png`
