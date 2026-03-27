# Thesis TTS Export

This repository now includes a small export pipeline that turns the main thesis chapters into a TTS-friendly plain text file.

## What it does

1. `scripts/merge_thesis_raw.py` reads `0-Config/4_files.tex` and merges the configured main chapters from `2-MainMatter` into one intermediate LaTeX file.
2. `scripts/clean_thesis_for_tts.py` removes LaTeX-specific markup, citations, labels, cross-references, figures, tables, and formatting noise to produce a plain text file for text-to-speech apps.
3. `scripts/export_thesis_tts.py` runs both steps in sequence.

The default outputs are written to `generated/tts/`:

- `generated/tts/thesis-merged.tex`
- `generated/tts/thesis-tts.txt`

## Usage

Run the full export:

```bash
python3 scripts/export_thesis_tts.py
```

Run only the merge step:

```bash
python3 scripts/merge_thesis_raw.py
```

Run only the cleanup step:

```bash
python3 scripts/clean_thesis_for_tts.py
```

Or use the Make target:

```bash
make tts
```

## Notes

- The export includes only the main chapters configured in `0-Config/4_files.tex`.
- Front matter, appendices, annexes, and the bibliography are excluded.
- Figure and table content is removed aggressively to keep the listening flow clean.
- If you later want a less aggressive version, the cleanup rules live in `scripts/clean_thesis_for_tts.py`.