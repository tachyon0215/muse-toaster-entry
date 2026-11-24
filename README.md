# muse-toaster-entry

Entry for the make.fun competition [The Funniest Toaster Error Message](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd).

## The entry

> E4: One side twice, the other not at all. I call it abstract. The smoke alarm disagrees.

Three candidates were drafted and compared against the judge brief (a real toaster error message first, freshness away from obvious toaster puns, tightness, one appliance voice, lands on a single read). This one won: uneven browning is a real toaster fault, the deadpan 'I call it abstract' is the appliance's own voice, and the smoke alarm's disagreement lands the punch in the last words. The alternatives (bread accepted / toast declined, warmed in its memory; crumb tray full, lower your expectations) were either poetic rather than an error or a stock expectations joke.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`, validates length/single-line/non-blank before writing, and reads the file back byte for byte. Running it twice produces identical bytes (sha256 55511fb7d5631ae888c235964ad5438031a92d76e026cb0365aff62afc7a015b).

## License

MIT — see [LICENSE](LICENSE).
