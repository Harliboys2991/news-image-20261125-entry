#!/usr/bin/env python3
"""Entry program for make.fun "Sum up 25 November's world news in one image"
(news-image-20261125).

The front page was drawn beforehand with draw_news.py and ships in this
repository as entry.png. This program copies it to the output directory
the grader reads. No network, no randomness, no clock: every run writes
exactly the same bytes.
"""
import os
import shutil
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
here = Path(__file__).resolve().parent
shutil.copyfile(here / "entry.png", out_dir / "entry.png")
