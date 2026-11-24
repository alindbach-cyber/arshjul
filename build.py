#!/usr/bin/env python3
"""Bygger årshjulet fra kildefilen.

    python3 build.py            -> dist/arshjul.html

Fra versjon 12 finnes det bare én utgave (enkel og team er slått sammen).
Byggeskriptet lager i tillegg to små videresendingssider med de gamle filnavnene
(arshjul-enkel.html og arshjul-team.html), så gamle lenker og bokmerker fortsatt virker.
Plassholder i src.html: __VERSION__.
"""
import re, sys, pathlib

VERSION = "12"
HERE = pathlib.Path(__file__).resolve().parent
OLD_NAMES = ("arshjul-enkel.html", "arshjul-team.html")

REDIRECT = """<!DOCTYPE html>
<html lang="no">
<head>
<meta charset="utf-8">
<title>Årshjul</title>
<meta http-equiv="refresh" content="0; url=arshjul.html">
<script>location.replace("arshjul.html" + location.hash);</script>
</head>
<body>
<p>Årshjulet har flyttet til <a href="arshjul.html">arshjul.html</a>. Oppgavene dine ligger der fortsatt.</p>
</body>
</html>
"""


def build(src: str) -> str:
    out = src.replace("__VERSION__", VERSION)
    leftovers = re.findall(r"<!--@/?\w+-->|/\*@/?\w+\*/|__(?:VERSION|EDITION)__", out)
    if leftovers:
        sys.exit(f"Rester av gamle merker eller plassholdere: {leftovers[:5]}")
    return out


def main():
    src = (HERE / "src.html").read_text(encoding="utf-8")
    dist = HERE / "dist"
    dist.mkdir(exist_ok=True)
    html = build(src)
    (dist / "arshjul.html").write_text(html, encoding="utf-8")
    print(f"arshjul.html: {len(html):,} tegn")
    for name in OLD_NAMES:
        (dist / name).write_text(REDIRECT, encoding="utf-8")
    print("videresending: " + ", ".join(OLD_NAMES))


if __name__ == "__main__":
    main()
