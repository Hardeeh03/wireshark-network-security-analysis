# Scripts

## capture_tshark.py
Capture packets with tshark for a fixed duration and save to the `captures/` folder.

**Usage**
```
python capture_tshark.py -i 1 -d 300
```

**Options**
- `-i`, `--interface`: Interface name or index (use `tshark -D` to list)
- `-d`, `--duration`: Capture duration in seconds (default: 300)
- `-o`, `--output`: Output file path (default: `captures/capture_<timestamp>.pcapng`)

**Example**
```
python capture_tshark.py -i Wi-Fi -d 180 -o ..\\captures\\sample_capture.pcapng
```
