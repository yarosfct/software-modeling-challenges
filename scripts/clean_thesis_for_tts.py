#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT_DIR / "generated" / "tts" / "thesis-merged.tex"
DEFAULT_OUTPUT = ROOT_DIR / "generated" / "tts" / "thesis-tts.txt"

SENTENCE_WITH_REF_PATTERNS = [
    re.compile(
        r"[^.?!\n]*\b(?:Chapter|Section|Subsection|Subsubsection|Appendix|Figure|Table)\s*~?\s*\\(?:ref|pageref)\{[^}]+\}[^.?!\n]*[.?!]?",
        re.IGNORECASE,
    ),
    re.compile(r"[^.?!\n]*\\(?:ref|pageref)\{[^}]+\}[^.?!\n]*[.?!]?"),
]

TEXT_COMMANDS = [
    "chapter",
    "section",
    "subsection",
    "subsubsection",
    "paragraph",
    "textbf",
    "textit",
    "texttt",
    "emph",
    "underline",
]

DROP_COMMANDS = [
    "typeout",
    "label",
    "cite",
    "nocite",
    "ref",
    "pageref",
    "includegraphics",
    "caption",
    "centering",
    "small",
    "footnotesize",
    "scriptsize",
    "normalsize",
    "large",
    "Large",
    "LARGE",
    "huge",
    "Huge",
    "setlength",
    "renewcommand",
    "toprule",
    "midrule",
    "bottomrule",
    "addlinespace",
    "hline",
    "noindent",
]


def strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*$", "", text, flags=re.MULTILINE)


def remove_environments(text: str) -> str:
    for env_name in [
        "figure",
        "table",
        "tabular",
        "tabularx",
        "longtable",
        "equation",
        "align",
        "align\\*",
        "gather",
        "gather\\*",
        "displaymath",
    ]:
        pattern = re.compile(
            rf"\\begin\{{{env_name}\}}(?:\[[^\]]*\])?.*?\\end\{{{env_name}\}}",
            re.DOTALL,
        )
        text = pattern.sub("\n", text)
    return text


def remove_sentences_with_refs(text: str) -> str:
    for pattern in SENTENCE_WITH_REF_PATTERNS:
        text = pattern.sub("\n", text)
    return text


def remove_drop_commands(text: str) -> str:
    for command in DROP_COMMANDS:
        text = re.sub(
            rf"\\{command}\*?(?:\[[^\]]*\])?(?:\{{[^{{}}]*\}})?(?:\{{[^{{}}]*\}})?",
            "",
            text,
        )
    return text


def replace_heading_commands(text: str) -> str:
    heading_patterns = {
        "chapter": "\n\n{title}\n\n",
        "section": "\n\n{title}\n\n",
        "subsection": "\n\n{title}\n\n",
        "subsubsection": "\n\n{title}\n\n",
        "paragraph": "\n\n{title} ",
    }

    for command, template in heading_patterns.items():
        pattern = re.compile(rf"\\{command}\*?(?:\[[^\]]*\])?\{{([^{{}}]*)\}}")
        text = pattern.sub(lambda match: template.format(title=match.group(1).strip()), text)

    return text


def unwrap_text_commands(text: str) -> str:
    changed = True
    while changed:
        changed = False
        for command in TEXT_COMMANDS:
            pattern = re.compile(rf"\\{command}\*?(?:\[[^\]]*\])?\{{([^{{}}]*)\}}")
            text, replacements = pattern.subn(r"\1", text)
            if replacements:
                changed = True
    return text


def replace_list_markup(text: str) -> str:
    text = re.sub(r"\\begin\{(?:itemize|enumerate)\}", "\n", text)
    text = re.sub(r"\\end\{(?:itemize|enumerate)\}", "\n", text)
    text = re.sub(r"\\item\s+", "\n- ", text)
    return text


def replace_inline_math(text: str) -> str:
    text = re.sub(r"\$\s*\\rightarrow\s*\$", " to ", text)
    text = re.sub(r"\$\s*([^$]+?)\s*\$", lambda match: clean_math_fragment(match.group(1)), text)
    return text


def clean_math_fragment(fragment: str) -> str:
    cleaned = fragment
    cleaned = cleaned.replace(r"\rightarrow", "to")
    cleaned = cleaned.replace(r"\to", "to")
    cleaned = cleaned.replace("{", "").replace("}", "")
    cleaned = cleaned.replace("_", " ")
    cleaned = re.sub(r"\\[A-Za-z]+", " ", cleaned)
    return f" {cleaned.strip()} "


def replace_generic_commands(text: str) -> str:
    changed = True
    while changed:
        changed = False
        pattern = re.compile(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}")
        text, replacements = pattern.subn(r"\1", text)
        if replacements:
            changed = True

    text = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?", "", text)
    return text


def normalize_punctuation(text: str) -> str:
    text = text.replace(r"\&", "&")
    text = text.replace(r"\%", "%")
    text = text.replace(r"\_", "_")
    text = text.replace(r"\#", "#")
    text = text.replace(r"\$", "$")
    text = text.replace(r"\{", "{")
    text = text.replace(r"\}", "}")
    text = text.replace(r"\ ", " ")
    text = text.replace(r"\.", ".")
    text = text.replace("~", " ")
    text = text.replace("``", '"')
    text = text.replace("''", '"')
    text = text.replace("“", '"')
    text = text.replace("”", '"')
    text = text.replace("–", " - ")
    text = text.replace("—", " - ")
    text = re.sub(r"(?<=\d)--(?=\d)", " to ", text)
    text = text.replace("---", " - ")
    text = text.replace("--", " - ")
    text = re.sub(r"([.?!]){2,}", r"\1", text)
    text = text.replace("\\newline", "\n")
    text = text.replace("\\\\", "\n")
    text = text.replace("\\par", "\n\n")
    return text


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"\s+([,.;:?!])", r"\1", text)
    text = re.sub(r"([.?!]){2,}", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    text = re.sub(r"\n-\s+", "\n- ", text)
    text = re.sub(r"\n- ([^\n]+?)\s*:\s*", r"\n- \1: ", text)
    return text.strip() + "\n"


def clean_text_for_tts(text: str) -> str:
    text = strip_comments(text)
    text = remove_environments(text)
    text = remove_sentences_with_refs(text)
    text = remove_drop_commands(text)
    text = replace_heading_commands(text)
    text = replace_list_markup(text)
    text = replace_inline_math(text)
    text = unwrap_text_commands(text)
    text = replace_generic_commands(text)
    text = normalize_punctuation(text)
    text = normalize_whitespace(text)
    return text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean merged thesis LaTeX into TTS-friendly plain text."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cleaned = clean_text_for_tts(args.input.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(cleaned, encoding="utf-8")
    print(f"Wrote cleaned TTS text to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())