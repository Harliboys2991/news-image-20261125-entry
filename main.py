#!/usr/bin/env python3
"""Submitted program for the make.fun bounty "Sum up 25 November's world
news in one image" (news-image-20261125).

draw_news.py rendered the front page ahead of time; it ships here as
entry.png. All this program does is copy that file into the output
directory the grader reads. No network, no randomness, no clock, so
every run writes exactly the same bytes.
"""
import os
import shutil
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
here = Path(__file__).resolve().parent
shutil.copyfile(here / "entry.png", out_dir / "entry.png")
