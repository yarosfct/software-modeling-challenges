---
name: cltsm-analysis
description: >-
  CLTSM thesis qualitative analysis conventions using Socio-Technical Grounded
  Theory (STGT) for software modelling education research. Use when coding
  transcripts, writing analytical memos, building cross-case comparisons,
  axial/selective coding, evidence maps, or editing files under Obsidian/CLTSM,
  interview-pilot, or paper-review. Prefer this skill over generic qualitative
  packs for vault layout, case IDs, templates, STGT stance, and evidence rules.
paths:
  - "Obsidian/CLTSM/**"
  - "interview-pilot/**"
  - "paper-review/**"
---

# CLTSM Analysis

Project-specific qualitative workflow for the CLTSM thesis (challenges of learning/teaching software modelling).

## Methodology: Socio-Technical Grounded Theory (STGT)

This thesis uses **Socio-Technical Grounded Theory (STGT)** (Hoda and related SE/STGT guidance), not classic Glaserian GT, Strauss–Corbin, or generic constructivist GT as the primary frame.

Implications for analysis and writing:

- Treat coding, memoing, constant comparison, theoretical sampling, and category development as **STGT-guided** practices adapted to socio-technical SE education settings.
- Prefer STGT vocabulary and procedures from the thesis methods chapter / STGT sources over generic GT pack defaults when they conflict.
- Generic skills in `qualitative-research-pro` (e.g. Glaserian GT, constructivist GT) are **craft references only** — adapt them to STGT; do not reframe the study as classic GT.
- Socio-technical lens: attend to interplay of people, practices, tools, pedagogy, and organisational/course conditions — not only individual cognition or only technology.

## Authority order

1. This skill and the live vault files (including the STGT stance above).
2. Project rule `.cursor/rules/cltsm-thesis-skills.mdc` for which other skills to load.
3. Generic packs (`qualitative-research-pro`, `academic-writer-skills`, `scholarly`) for method/writing craft only — never override case IDs, paths, templates, or the STGT methodology here.

## Single analysis home

All qualitative analysis lives under **`Obsidian/CLTSM/`**. There is no root `qualitative_analysis/` tree.

| Stage | Path | Status |
|---|---|---|
| Transcripts | `Obsidian/CLTSM/qualitative_analysis/01_raw_transcripts/` | 10 standardized cases (`L*_transcript.md`, `S*_transcript.md`) |
| First-cycle coding | `…/02_first_cycle_coding/{Case}/` | One note per code `{Case}-Cnn.md` + `index.md` (see habit note) |
| Memos | `…/03_memos/` | Short idea memos `{Case}M{n}.md` (see habit note) |
| Cross-case | `…/04_cross_case_analysis/` | Inventory, evidence map, findings guide |
| Habit note | `…/stgt_coding_memo_habit.md` | Coding + memo simplicity rules |
| Category canvas habit | `…/stgt_category_canvas_habit.md` | Per-CAT evidence canvases + coding layout |
| Canvas map habit | `…/stgt_canvas_map_habit.md` | Coordinator-friendly findings canvases |
| Findings canvases | `Obsidian/CLTSM/canvases/` | Overview, relations, `categories/CAT….canvas` |

Do not recreate parallel analysis folders at the repo root.

## Related project folders

| Path | Role |
|---|---|
| `interview-pilot/pilot-student.md` | Student interview guide (Variants A/B/C + pt-PT appendix) |
| `interview-pilot/pilot-teacher.md` | Lecturer interview guide (Variants A/B/C) |
| `paper-review/literature-index.md` | Short paper → thesis-use map |
| `paper-review/cards/` | Concise per-paper cards |
| `papers/` | Source PDF store (do not duplicate as long digests) |

## Case IDs

- Lecturers: **L1–L4**
- Students: **S1–S6**
- Codes: `{Case}-C{nn}` in `02_first_cycle_coding/{Case}/` (e.g. `S4-C02`)
- Memos: `{Case}M{n}` (e.g. `S4M1`, `L3M10`)

Treat all cases as ordinary interview sources. Do not invent reconstruction/provenance cautions.

## Transcript conventions

Each transcript uses YAML frontmatter (`case_id`, `role`, `version`, `timestamp_style`) and speakers **`Interviewer` / `Participant`** only. Preserve existing timestamps; never invent them.

## Evidence chain (mandatory)

1. **Turn** in transcript (`<!-- T00n -->`)
2. **Open code** note `02_first_cycle_coding/{Case}/{Case}-Cnn.md` (natural language)
3. **Memo** in `03_memos/{Case}M{n}.md` linking codes + turns
4. **Category / findings canvas** from those IDs (`canvases/categories/`, overview)

Follow **`Obsidian/CLTSM/qualitative_analysis/stgt_coding_memo_habit.md`** for formats, density, and simplicity rules.

Never invent quotes. Prefer Obsidian MCP vault search when available.

Distinguish:

- Student direct evidence
- Lecturer interpretation of student behaviour
- Design implications / tool proposals (not validated intervention effects)

## Coding & memos (lightweight STGT)

- Codes: plain English titles; always cite turn IDs; keep sheets short.
- Memos: one idea each; link codes + turns; 2–5 sentence core; one open question.
- Traceability: update transcripts with `<!-- T00n -->` markers; do not invent timestamps.
- Naming: `coding_S1C.md`, `S1-C01`, `S1M1`, etc.
- Avoid GT jargon packs overriding this habit; adapt `open-coding` / `memo-writing` craft to this file.

## Cross-case work (when resumed)

Rebuild under `04_cross_case_analysis/` from new memos/codes. Prefer bounded, conditional claims with memo/case IDs. Do not claim theoretical saturation unless asked to evaluate it.

## Obsidian / MCP usage

When Obsidian MCP Connector is available:

- Prefer vault search/read tools for locating notes and tags.
- Preserve wikilinks `[[like this]]` when editing.

## What not to do

- Do not invent cases, quotes, codes, or memo IDs.
- Do not silently rename case IDs or folder conventions.
- Do not convert lecturer interpretations into student-reported facts.
- Do not treat tool/AI proposals as empirically validated results.
- Do not restore deleted audio, old digests, or dual analysis trees unless the user asks.
