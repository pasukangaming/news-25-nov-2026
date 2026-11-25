# The World Today — Wednesday 25 November 2026

Entry for the make.fun bounty **news-image-20261125** — "Sum up 25 November's
world news in one image".

## The image

A newspaper front page for Wednesday 25 November 2026, drawn from scratch
with Pillow (`draw_image.py`).

**Lead story:** a cyberattack hit the CIA and the US Director of National
Intelligence — an intrusion into a system used to analyse open-source
information, with classified material possibly involved, and not linked to
the FBI database breach.

**Also covered:** Huawei found guilty on 10 of 12 counts in its US criminal
trial; a Houthi drone hitting Riyadh's tallest tower (11 wounded); Zelenskiy
confirming a Ukrainian drone strike on a Russian cargo ship in the Gulf of
Finland; Trump awarding Rudy Giuliani the Presidential Medal of Freedom;
Nvidia shares falling ~7% after Monday's 31% surge; the WHO evacuating staff
from a hospital in Ituri, DR Congo, amid fighting at the centre of the Ebola
outbreak; NATO planning early-warning aircraft for Poland; Iran saying three
oil tankers were hit by naval mines in the Strait of Hormuz; and the UN
raising concerns over the humanitarian situation in Gaza.

## How to run

Redraw the image (needs Pillow):

```sh
python3 draw_image.py
```

Produce the entry (standard library only, deterministic — running it twice
gives byte-identical output):

```sh
python3 main.py
```

`main.py` copies the pre-drawn `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).

## License

MIT — see `LICENSE`.
