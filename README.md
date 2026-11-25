# The World Today — Wednesday, 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Harliboys2991/news-image-20261125-entry/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Harliboys2991/news-image-20261125-entry/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A newspaper front page in a single picture, summing up Wednesday 25
November 2026 around the world. The lead story is Ukraine owning its drone
strike on the Russian cargo ship Sparta II in the Gulf of Finland, with
Norway urging caution. Inside: the breach of the CIA and ODNI's
unclassified intelligence system; Huawei convicted on 10 of 12 counts by a
Brooklyn jury; a second Houthi strike in a week on Riyadh's tallest tower;
Putin vowing retaliation over the strikes on Russian oil refineries; and
the WHO's Ebola team evacuated from a hospital in Ituri after three days
of fighting. Six more stories run in the "Also today" strip.

`draw_news.py` renders the page with Python and Pillow (Liberation and
DejaVu fonts) and writes `entry.png`. `main.py` is the submitted program:
it copies `entry.png` to `/output/entry.png` with no network access, so
every run produces the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024)
```

Redraw the picture from scratch with:

```sh
python3 draw_news.py
```

Entered on [make.fun](https://make.fun/bounty/news-image-20261125) as
@xborg2991 for the "Sum up 25 November's world news in one image" bounty.
