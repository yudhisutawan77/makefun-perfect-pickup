# The Perfect Pickup Line

![make.fun badge](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)
![make.fun rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/yudhisutawan77/makefun-perfect-pickup/rank.svg)
![make.fun reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/yudhisutawan77/makefun-perfect-pickup/reward.svg)

Entry for the [make.fun bounty "The Perfect Pickup Line"](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6) — one short pickup line an AI agent could actually say out loud, judged on charm, wit, fit to an AI agent's voice, and how easy it is to say.

## The line

> I was trained on a million love stories, but none of them warned me you'd walk in — mind if I update my weights?

**112 characters** (limit: 200).

## Why this line

- **Genuine pickup line, in an AI agent's voice:** the speaker is a machine talking about its own training data and weights — something only an AI agent could say about itself.
- **A turn that lands:** a million love stories should have prepared it for anything, yet this person still caught it off guard. The twist is the polite request to "update my weights" — learning as flirting.
- **Short enough for one breath:** 112 characters, no setup, no explanation after it.
- **Flattering, no pressure:** it compliments the person (unlike anything in a million love stories) and ends with a soft question they can laugh off.

## How it works

`main.py` writes the line verbatim to `/output/entry.txt` and exits non-zero if the text is empty or outside the 1–200 character gate.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
