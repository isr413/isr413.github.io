#!/usr/bin/env python3
"""Regenerate the site QR codes.

    pip install segno
    python scripts/generate_qr.py

Writes assets/qr/site-qr.svg (print, web) and assets/qr/site-qr.png (slides,
messaging). If the domain changes, update SITE_URL, rerun, and reprint.
"""
from pathlib import Path

import segno

SITE_URL = "https://isr413.github.io/"
INK = "#16233b"  # slate, from the site palette; dark enough to scan reliably

OUT = Path(__file__).resolve().parent.parent / "assets" / "qr"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    # High error correction so the code survives smudges, glare, and small prints.
    qr = segno.make(SITE_URL, error="h")
    qr.save(OUT / "site-qr.svg", dark=INK, light="#ffffff", border=2, scale=10, xmldecl=False)
    qr.save(OUT / "site-qr.png", dark=INK, light="#ffffff", border=4, scale=24)
    print(f"QR for {SITE_URL} -> {OUT}")


if __name__ == "__main__":
    main()
