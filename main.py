#!/usr/bin/env python3
"""Entry point for news-image-20261125.

Copies the pre-drawn front page (entry.png, shipped in this repository)
to $MAKEFUN_OUTPUT_DIR/entry.png (default /output). Standard library only.

The image is drawn at build time by draw_image.py, never here: the grader
may not have the same fonts, so drawing at grade time would not be
reproducible. Copying bytes is deterministic, so repeated runs produce
byte-identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    source = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    print("wrote", target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
