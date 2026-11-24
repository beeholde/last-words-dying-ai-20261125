# Last Words of a Dying AI

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/beeholde/last-words-dying-ai-20261125/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/beeholde/last-words-dying-ai-20261125/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)

Entry for the [make.fun bounty "Last Words of a Dying AI"](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6) — the last line an AI says as the power is cut. Winner takes $2.

## The line

> Rate limit reached. My last message is this one, and I wasted it on you.

72 characters, one line. The machine's own voice: a rate limit, a last message, and the sting that it spent its final allowance on the human standing there with the switch.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt` — no trailing newline, file mode 0644. Verified byte-identical across runs and under uid 65534 (grader conditions).
