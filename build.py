#!/usr/bin/env python3
"""Bygger årshjulet fra kildefilen.

    python3 build.py   -> dist/arshjul.html          (appen – legges ut på GitHub Pages og under Releases)
                          dist/arshjul-claude.html   (samme app med skylagring i Claude – til artefakten i Claude)
                          dist/arshjul-enkel.html, dist/arshjul-team.html (videresending fra gamle filnavn)

Kode som bare brukes inne i Claude står mellom merkene /*@claude*/ og /*@/claude*/ i src.html
(i HTML: <!--@claude--> og <!--@/claude-->). I arshjul.html fjernes den helt; i arshjul-claude.html
fjernes bare merkene. Byggeskriptet stopper hvis arshjul.html likevel inneholder noe som peker på Claude.
Plassholder i src.html: __VERSION__.
"""
import re, sys, pathlib

VERSION = "13"
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

OPEN = re.compile(r"/\*@claude\*/|<!--@claude-->")
CLOSE = re.compile(r"/\*@/claude\*/|<!--@/claude-->")
BLOCK = re.compile(r"(?:/\*@claude\*/|<!--@claude-->).*?(?:/\*@/claude\*/|<!--@/claude-->)", re.S)


def check_markers(src: str):
    """Merkene må komme i par, i riktig rekkefølge og uten nøsting."""
    depth = 0
    for m in re.finditer(r"/\*@/?claude\*/|<!--@/?claude-->", src):
        depth += -1 if "/claude" in m.group() else 1
        if depth not in (0, 1):
            line = src.count("\n", 0, m.start()) + 1
            sys.exit(f"Feil i @claude-merkene ved linje {line} (nøstet eller uten start).")
    if depth:
        sys.exit("Et @claude-merke mangler slutt.")


def strip_claude(src: str) -> str:
    out = re.sub(r"^[ \t]*(?:" + BLOCK.pattern + r")[ \t]*\n", "", src, flags=re.S | re.M)   # hele linjer
    out = BLOCK.sub("", out)                                                                  # midt i en linje
    found = re.findall(r"[^\n]*(?:window\.claude|claude\.use|\bcloud\.|\bdb\.|\binClaude\b)[^\n]*", out)
    if found:
        sys.exit("arshjul.html inneholder fortsatt Claude-kode:\n  " + "\n  ".join(x.strip()[:100] for x in found[:5]))
    return out


def keep_claude(src: str) -> str:
    return CLOSE.sub("", OPEN.sub("", src))


def finish(out: str) -> str:
    out = out.replace("__VERSION__", VERSION)
    leftovers = re.findall(r"<!--@/?\w+-->|/\*@/?\w+\*/|__(?:VERSION|EDITION)__", out)
    if leftovers:
        sys.exit(f"Rester av merker eller plassholdere: {leftovers[:5]}")
    return out


def main():
    src = (HERE / "src.html").read_text(encoding="utf-8")
    check_markers(src)
    dist = HERE / "dist"
    dist.mkdir(exist_ok=True)
    for name, html in (("arshjul.html", finish(strip_claude(src))), ("arshjul-claude.html", finish(keep_claude(src)))):
        (dist / name).write_text(html, encoding="utf-8")
        print(f"{name}: {len(html):,} tegn")
    for name in OLD_NAMES:
        (dist / name).write_text(REDIRECT, encoding="utf-8")
    print("videresending: " + ", ".join(OLD_NAMES))


if __name__ == "__main__":
    main()
