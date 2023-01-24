#!/usr/bin/env python3
import sys


def generate_timeline(specified_event: str = "Climate change") -> None:
    print(f"Generating timeline for the `{specified_event}`")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        event: str = sys.argv[1]
        generate_timeline(event)
    else:
        generate_timeline()
