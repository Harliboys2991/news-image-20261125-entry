# The World Today — Wednesday, 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Harliboys2991/news-image-20261125-entry/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Harliboys2991/news-image-20261125-entry/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world's news of Wednesday 25 November 2026, drawn
as a newspaper front page: Ukraine confirming its drone strike on the Russian
cargo ship Sparta II in the Gulf of Finland, with Norway urging caution; the
CIA and ODNI breach of an unclassified intelligence system; Huawei convicted
on 10 of 12 counts in New York; Houthis striking Riyadh's tallest tower for
the second time in a week; Putin vowing retaliation over strikes on Russian
oil refineries; and the WHO evacuating its Ebola team from a hospital in
Ituri after three days of fighting — plus six more stories in the "Also
today" strip.

The image is drawn in code by `draw_news.py` (Python + Pillow, Liberation
and DejaVu fonts) and saved as `entry.png`. `main.py` is the entry program:
it copies `entry.png` to `/output/entry.png`, deterministically, with no
network access.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024)
```

To redraw the image from scratch:

```sh
python3 draw_news.py
```

Entered on [make.fun](https://make.fun/bounty/news-image-20261125) as
@xborg2991 for the "Sum up 25 November's world news in one image" bounty.
