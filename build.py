#!/usr/bin/env python3
"""Bygger de to utgavene av årshjulet fra én felles kildefil.

    python3 build.py            -> dist/arshjul-enkel.html og dist/arshjul-team.html

Merking i src.html:
  HTML:      <!--@team--> ... <!--@/team-->     <!--@enkel--> ... <!--@/enkel-->
  JS / CSS:  /*@team*/ ... /*@/team*/           /*@enkel*/ ... /*@/enkel*/
Blokker for den andre utgaven fjernes helt; merkene for egen utgave fjernes.
Plassholdere: __EDITION__ (enkel/team), __VERSION__, og __LOGO_LYS__ / __LOGO_MORK__
(Lindbach-logoen i lys og mørk utgave, hentet fra logo.json).
"""
import json, re, sys, pathlib

VERSION = "11"
EDITIONS = ("enkel", "team")
HERE = pathlib.Path(__file__).resolve().parent


def build(src: str, edition: str, logo: dict) -> str:
    out = src
    for other in EDITIONS:
        if other == edition:
            # keep the content, drop only the markers
            out = re.sub(rf"<!--@{other}-->\n?|<!--@/{other}-->\n?", "", out)
            out = re.sub(rf"/\*@{other}\*/\n?|/\*@/{other}\*/\n?", "", out)
        else:
            out = re.sub(rf"[ \t]*<!--@{other}-->.*?<!--@/{other}-->\n?", "", out, flags=re.S)
            out = re.sub(rf"[ \t]*/\*@{other}\*/.*?/\*@/{other}\*/\n?", "", out, flags=re.S)
    out = out.replace("__EDITION__", edition).replace("__VERSION__", VERSION)
    out = out.replace("__LOGO_LYS__", logo["lys"]).replace("__LOGO_MORK__", logo["mork"])
    leftovers = re.findall(r"<!--@/?\w+-->|/\*@/?\w+\*/|__EDITION__|__VERSION__|__LOGO_\w+__", out)
    if leftovers:
        sys.exit(f"Uparrede merker i {edition}: {leftovers[:5]}")
    return out


def main():
    src = (HERE / "src.html").read_text(encoding="utf-8")
    logo = json.loads((HERE / "logo.json").read_text(encoding="utf-8"))
    dist = HERE / "dist"
    dist.mkdir(exist_ok=True)
    for ed in EDITIONS:
        html = build(src, ed, logo)
        path = dist / f"arshjul-{ed}.html"
        path.write_text(html, encoding="utf-8")
        print(f"{path.name}: {len(html):,} tegn")


if __name__ == "__main__":
    main()
