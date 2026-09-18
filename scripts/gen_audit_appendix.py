#!/usr/bin/env python3
"""Generate compact LaTeX cards from vault memos and code notes. Read-only on vault."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/home/wiirijo/Documents/Fac/software-modeling-challenges")
MEMO_DIR = ROOT / "Obsidian/CLTSM/qualitative_analysis/03_memos"
CODE_ROOT = ROOT / "Obsidian/CLTSM/qualitative_analysis/02_first_cycle_coding"
OUT = ROOT / "3-BackMatter"

MEMOS = [
    "S3M1", "S8M1", "L1M1", "S1M1", "S3M3", "S2M3", "S6M2", "S4M2", "S10M5",
    "S6M1", "S10M1", "S7M5", "S1M2", "S7M1", "L4M6", "S5M3", "S1M5", "S7M3",
    "S10M3", "S4M3", "S8M2", "S10M2", "S4M5", "S5M4", "S10M4", "S3M4", "S7M2",
    "L4M5", "S1M4", "L1M5", "S4M1", "L4M3", "L1M3", "S7M6", "S8M3",
]

CODES = [
    "S1/S1-C04", "S1/S1-C12", "S1/S1-C08", "S1/S1-C23", "S2/S2-C08", "S2/S2-C04",
    "S3/S3-C04", "S4/S4-C02", "S4/S4-C08", "S5/S5-C04", "S6/S6-C01", "S7/S7-C09",
    "S7/S7-C16", "S8/S8-C01", "S10/S10-C02", "S10/S10-C11", "S10/S10-C12",
]


def latex_escape(text: str) -> str:
    text = text.replace("\\", "\\textbackslash{}")
    repl = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for k, v in repl.items():
        text = text.replace(k, v)
    text = text.replace("—", "---").replace("–", "--")
    text = text.replace("“", "``").replace("”", "''").replace("‘", "`").replace("’", "'")
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\\texttt{\1}", text)
    return text


def section_after(md: str, heading: str) -> str:
    pat = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    m = re.search(pat, md, re.M | re.S)
    return m.group(1).strip() if m else ""


def field(md: str, name: str) -> str:
    m = re.search(rf"^- {name}:\s*(.+)$", md, re.M)
    return m.group(1).strip() if m else ""


def parse_memo(mid: str) -> dict:
    path = MEMO_DIR / f"{mid}.md"
    md = path.read_text(encoding="utf-8")
    title_line = md.splitlines()[0]
    title = re.sub(rf"^# {re.escape(mid)}\s+[—-]\s+", "", title_line).strip()
    return {
        "id": mid,
        "title": title,
        "case": field(md, "Case"),
        "codes": field(md, "Codes"),
        "turns": field(md, "Turns"),
        "idea": section_after(md, "Idea"),
        "why": section_after(md, "Why it matters"),
    }


def parse_code(rel: str) -> dict:
    path = CODE_ROOT / f"{rel}.md"
    md = path.read_text(encoding="utf-8")
    title_line = md.splitlines()[0]
    cid = rel.split("/")[-1]
    title = re.sub(rf"^# {re.escape(cid)}\s+[—-]\s+", "", title_line).strip()
    quote = section_after(md, "Quote")
    quote = quote.strip().strip('"').strip()
    quote = quote.replace('\\"', '"').replace('\\', '')
    note = section_after(md, "Note")
    return {
        "id": cid,
        "title": title,
        "case": field(md, "Case"),
        "turns": field(md, "Turns"),
        "quote": quote,
        "note": note,
    }


def memo_card(d: dict) -> str:
    return (
        "\\begin{tcolorbox}[colback=gray!4,colframe=black!35,boxrule=0.4pt,"
        "left=3pt,right=3pt,top=2pt,bottom=2pt,arc=1pt,"
        f"title={{\\small\\textbf{{{latex_escape(d['id'])}}} --- {latex_escape(d['title'])}}}]\n"
        "\\footnotesize "
        f"\\textbf{{Case:}} {latex_escape(d['case'])}. "
        f"\\textbf{{Codes:}} {latex_escape(d['codes'])}. "
        f"\\textbf{{Turns:}} {latex_escape(d['turns'])}.\n\n"
        f"\\textit{{Idea.}} {latex_escape(d['idea'])}\n\n"
        f"\\textit{{Why it matters.}} {latex_escape(d['why'])}\n"
        "\\end{tcolorbox}\n\\vspace{2pt}\n"
    )


def code_card(d: dict) -> str:
    note = f"\n\n\\textit{{Note.}} {latex_escape(d['note'])}" if d["note"] else ""
    return (
        "\\begin{tcolorbox}[colback=blue!3,colframe=black!35,boxrule=0.4pt,"
        "left=3pt,right=3pt,top=2pt,bottom=2pt,arc=1pt,"
        f"title={{\\small\\textbf{{{latex_escape(d['id'])}}} --- {latex_escape(d['title'])}}}]\n"
        "\\footnotesize "
        f"\\textbf{{Case:}} {latex_escape(d['case'])}. "
        f"\\textbf{{Turns:}} {latex_escape(d['turns'])}.\n\n"
        f"\\textit{{Quote.}} ``{latex_escape(d['quote'])}''"
        f"{note}\n"
        "\\end{tcolorbox}\n\\vspace{2pt}\n"
    )


def main() -> None:
    memos_tex = "% auto-generated from vault memos --- do not edit by hand\n"
    for mid in MEMOS:
        memos_tex += memo_card(parse_memo(mid))
    (OUT / "appendix_audit_memos.tex").write_text(memos_tex, encoding="utf-8")

    codes_tex = "% auto-generated from vault code notes --- do not edit by hand\n"
    for rel in CODES:
        codes_tex += code_card(parse_code(rel))
    (OUT / "appendix_audit_codes.tex").write_text(codes_tex, encoding="utf-8")
    print(f"wrote {len(MEMOS)} memos, {len(CODES)} codes")


if __name__ == "__main__":
    main()
