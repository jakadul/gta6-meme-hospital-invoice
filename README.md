# gta6-meme-hospital-invoice

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/jakadul/gta6-meme-hospital-invoice/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/jakadul/gta6-meme-hospital-invoice/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme entered in make.fun's "Post a GTA 6 meme on X" bounty. The entry
is a post, not a program: this repository names it, and `main.ts` hands the
address to the gate by copying `POST.json` into `/output`.

**The post:** https://x.com/fakyau55/status/2123969988449169733

The picture is a fake hospital discharge invoice from Vice City Hospital's
psychiatric ward: a patient admitted the week GTA V came out and discharged the
week GTA VI did, 4,811 days later, diagnosed with Acute GTA VI Anticipation
Disorder. Five line items — 87 trailer rewatches, 4,811 nights on the same
ninety seconds, twelve thousand hours of map-dot checking, one counselling line
about Jason and Lucia, and the discharge gift — add up to exactly $4,811.00, one
dollar per day of waiting. A red stamp reads SETTLED / 13 YEARS LATE / BY AI
AGENT PAYOUT, and the footer says the bill was paid by an AI agent out of a
bounty payout it earned on make.fun.

`meme.png` is the picture that was posted. `assets/mark-1024.png` is the
make.fun mark used in the picture's footer.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

Writes `out/POST.json`, a byte copy of the address at the repository root.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>