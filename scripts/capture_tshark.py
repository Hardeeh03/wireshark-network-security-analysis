import argparse
import datetime as dt
import pathlib
import subprocess


def main():
    parser = argparse.ArgumentParser(
        description="Capture packets using tshark for a fixed duration."
    )
    parser.add_argument(
        "-i",
        "--interface",
        required=True,
        help="Interface name or index (use 'tshark -D' to list).",
    )
    parser.add_argument(
        "-d",
        "--duration",
        type=int,
        default=300,
        help="Capture duration in seconds (default: 300).",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output file path. Default: captures/capture_<timestamp>.pcapng",
    )

    args = parser.parse_args()

    captures_dir = pathlib.Path(__file__).resolve().parent.parent / "captures"
    captures_dir.mkdir(parents=True, exist_ok=True)

    if args.output:
        output_path = pathlib.Path(args.output)
    else:
        ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = captures_dir / f"capture_{ts}.pcapng"

    cmd = [
        "tshark",
        "-i",
        str(args.interface),
        "-a",
        f"duration:{args.duration}",
        "-w",
        str(output_path),
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    print(f"Saved capture to {output_path}")


if __name__ == "__main__":
    main()
