#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT_DIR / "0-Config" / "4_files.tex"
DEFAULT_CHAPTER_DIR = ROOT_DIR / "2-MainMatter"
DEFAULT_OUTPUT = ROOT_DIR / "generated" / "tts" / "thesis-merged.tex"


def strip_latex_comment(line: str) -> str:
    return re.sub(r"(?<!\\)%.*$", "", line)


def extract_chapter_names(config_text: str) -> list[str]:
    chapter_names: list[str] = []
    pattern = re.compile(r"\\ntaddfile\{chapter\}(?:\[[^\]]+\])?\{([^}]+)\}")

    for raw_line in config_text.splitlines():
        line = strip_latex_comment(raw_line).strip()
        if not line:
            continue
        match = pattern.search(line)
        if match:
            chapter_names.append(match.group(1).strip())

    if not chapter_names:
        raise ValueError("No chapter entries were found in the thesis config.")

    return chapter_names


def merge_chapters(config_path: Path, chapter_dir: Path, output_path: Path) -> list[Path]:
    chapter_names = extract_chapter_names(config_path.read_text(encoding="utf-8"))
    merged_chunks: list[str] = []
    resolved_paths: list[Path] = []

    for chapter_name in chapter_names:
        chapter_path = chapter_dir / f"{chapter_name}.tex"
        if not chapter_path.exists():
            raise FileNotFoundError(f"Configured chapter file not found: {chapter_path}")
        resolved_paths.append(chapter_path)
        merged_chunks.append(chapter_path.read_text(encoding="utf-8").strip())

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n".join(merged_chunks) + "\n", encoding="utf-8")
    return resolved_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Merge thesis main chapters into a single intermediate LaTeX file."
    )
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--chapter-dir", type=Path, default=DEFAULT_CHAPTER_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    merged_paths = merge_chapters(args.config, args.chapter_dir, args.output)
    print(f"Merged {len(merged_paths)} chapters into {args.output}")
    for path in merged_paths:
        print(f" - {path.relative_to(ROOT_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())