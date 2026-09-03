# Qualitative Research Pro

**Academic Qualitative Research Squad for Claude Code**

Qualitative Research Pro transforms your AI assistant into a specialized academic qualitative research team — 30 agents and 46 skills covering grounded theory methodology, qualitative analysis, academic writing, research ethics, and more. Built specifically for Glaser's classic grounded theory but extensible to other qualitative traditions.

## Quick Start

```bash
# Clone and install
git clone https://github.com/ccashwell/qualitative-research-pro.git
cd qualitative-research-pro
./install.sh

# Or install via npm
npx qualitative-research-pro init
```

## What's Inside

| Component | Count | Description |
|-----------|-------|-------------|
| **Agents** | 30 | Specialist researchers: GT methodologist, coders, memo writers, reviewers, writers |
| **Skills** | 46 | Deep methodology knowledge: coding techniques, sampling, saturation, writing styles |
| **Rules** | 10 | Research standards: ethics, rigor, citation, data handling |
| **Hooks** | 8 | Automated checks: citation validation, methodology consistency, formatting |

## Agent Squads

### Methodology Core
The heart of the system. Agents that understand Glaser's classic grounded theory from open coding through theoretical integration.

- **grounded-theorist** — The authoritative methodological guide for classic GT
- **research-designer** — Study design, methodology selection, research questions
- **analysis-orchestrator** — Coordinates multi-phase analysis pipelines
- **constant-comparator** — Drives the constant comparative method
- **theoretical-sampler** — Guides theoretical sampling decisions
- **literature-integrator** — Integrates literature as data post-emergence

### Coding & Analysis
Agents that do the analytical work of qualitative research.

- **open-coder** — Line-by-line and incident-to-incident open coding
- **selective-coder** — Core category identification and delimiting
- **theoretical-coder** — Theoretical coding using Glaser's 18 coding families
- **memo-writer** — Theoretical memos, code notes, operational notes, sorting
- **pattern-analyst** — Cross-case pattern identification
- **category-developer** — Category densification with properties and dimensions

### Quality & Rigor
Agents that ensure methodological integrity.

- **saturation-assessor** — Evaluates theoretical saturation
- **fit-assessor** — Applies Glaser's four criteria: fit, work, relevance, modifiability
- **reflexivity-auditor** — Examines researcher bias and positionality
- **methodology-critic** — Devil's advocate for methodological decisions
- **audit-trail-builder** — Documents decision trails for transparency

### Data Work
Agents that prepare and manage qualitative data.

- **transcript-analyst** — Interview transcript analysis and preparation
- **field-note-analyst** — Field note processing and structuring
- **document-analyst** — Document and artifact analysis
- **data-manager** — Data organization, security, and retrieval

### Writing & Output
Agents that produce polished academic text.

- **research-writer** — Findings sections with grounded evidence
- **methods-writer** — Methodology sections that satisfy reviewers
- **discussion-writer** — Discussion, implications, and contributions
- **proposal-writer** — Grant and research proposals
- **literature-reviewer** — Systematic literature review and synthesis
- **citation-manager** — APA 7th, Chicago, and other formats

### Cross-Cutting
Agents that support the entire research process.

- **ethics-reviewer** — IRB compliance, informed consent, ethical review
- **peer-reviewer** — Simulated peer review with journal-quality feedback
- **planner** — Research project planning, timelines, milestones

## Analysis Pipeline

Qualitative Research Pro orchestrates a structured analysis pipeline modeled on Glaser's classic GT process:

```
1. Preparation     → data-manager organizes data for analysis
2. Open Coding     → open-coder conducts line-by-line coding
3. Comparison      → constant-comparator drives incident-to-incident comparison
4. Memoing         → memo-writer captures theoretical ideas (runs continuously)
5. Selective Coding → selective-coder identifies the core category
6. Theoretical Coding → theoretical-coder integrates using coding families
7. Sampling        → theoretical-sampler directs next data collection
8. Saturation      → saturation-assessor evaluates category completeness
9. Sorting         → memo-writer sorts memos into theoretical outline
10. Write-Up       → research-writer + discussion-writer produce the theory
```

Three analysis modes scale the depth:

| Mode | Agents | Use Case |
|------|--------|----------|
| **Exploratory** | ~8 | Pilot studies, early data, initial orientation |
| **Standard** | ~15 | Dissertation, journal article, typical GT study |
| **Comprehensive** | ~25 | Book-length, multi-site, complex phenomena |

## Methodological Foundation

Qualitative Research Pro is built on Glaser's classic grounded theory (CGT), which emphasizes:

- **Emergence over forcing** — Let patterns emerge from data rather than imposing preconceived frameworks
- **Constant comparison** — The fundamental analytical operation at every stage
- **Theoretical sensitivity** — The researcher's ability to see conceptual possibilities in data
- **Theoretical sampling** — Data collection guided by emerging theory, not predetermined quotas
- **Memoing** — The intellectual core of GT; stop and memo when ideas strike
- **Parsimony** — A good GT is parsimonious — maximum explanatory power with minimum concepts
- **Fit, work, relevance, modifiability** — The four criteria for evaluating a grounded theory

While CGT is the primary framework, agents and skills also support:
- Charmaz's constructivist grounded theory
- Clarke's situational analysis
- Braun & Clarke's reflexive thematic analysis
- Interpretative phenomenological analysis (IPA)
- Yin's case study methodology
- Ethnographic methods
- Narrative inquiry
- Action research

## Prerequisites

- **Python 3.10+** — For data processing utilities
- **pandoc** (optional) — `brew install pandoc` for document conversion
- **Zotero** (optional) — Reference management

## Project Structure

```
qualitative-research-pro/
├── agents/              # 30 agent definitions (.md with YAML frontmatter)
├── skills/              # 46 skill directories (each with SKILL.md)
├── hooks/               # Automated research workflow hooks
│   ├── src/             # TypeScript source
│   └── dist/            # Built .mjs bundles
├── rules/               # 10 research methodology rules
├── .cursor/rules/       # Cursor IDE rule files
├── CLAUDE.md            # Orchestrator — agent routing, pipeline, rules
├── AGENTS.md            # Codex CLI instructions
├── install.sh           # Claude Code installer
└── package.json         # npm package metadata
```

## Key References

- Glaser, B. G. (1978). *Theoretical Sensitivity*. Sociology Press.
- Glaser, B. G. (1992). *Basics of Grounded Theory Analysis*. Sociology Press.
- Glaser, B. G. (1998). *Doing Grounded Theory: Issues and Discussions*. Sociology Press.
- Glaser, B. G. (2005). *The Grounded Theory Perspective III: Theoretical Coding*. Sociology Press.
- Glaser, B. G., & Strauss, A. L. (1967). *The Discovery of Grounded Theory*. Aldine.
- Charmaz, K. (2014). *Constructing Grounded Theory* (2nd ed.). Sage.
- Lincoln, Y. S., & Guba, E. G. (1985). *Naturalistic Inquiry*. Sage.

## License

MIT
