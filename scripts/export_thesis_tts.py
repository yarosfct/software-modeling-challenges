#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
MERGE_SCRIPT = ROOT_DIR / "scripts" / "merge_thesis_raw.py"
CLEAN_SCRIPT = ROOT_DIR / "scripts" / "clean_thesis_for_tts.py"
DEFAULT_MERGED = ROOT_DIR / "generated" / "tts" / "thesis-merged.tex"
DEFAULT_OUTPUT = ROOT_DIR / "generated" / "tts" / "thesis-tts.txt"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export thesis main chapters to a TTS-friendly plain text file."
    )
    parser.add_argument("--merged-output", type=Path, default=DEFAULT_MERGED)
    parser.add_argument("--tts-output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    subprocess.run(
        [sys.executable, str(MERGE_SCRIPT), "--output", str(args.merged_output)],
        check=True,
        cwd=ROOT_DIR,
    )
    subprocess.run(
        [
            sys.executable,
            str(CLEAN_SCRIPT),
            "--input",
            str(args.merged_output),
            "--output",
            str(args.tts_output),
        ],
        check=True,
        cwd=ROOT_DIR,
    )

    print(f"Created TTS export at {args.tts_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())