# Qualitative Research Pro

**Academic Qualitative Research Squad**

This file is for **Codex CLI** (OpenAI). If you're using Claude Code, see `CLAUDE.md` or just run `./install.sh`.

## What is this?

Qualitative Research Pro turns your AI coding assistant into a specialized academic qualitative research team. Agents cover methodology design, grounded theory coding, memoing, theoretical sampling, literature review, academic writing, and research ethics — everything needed to conduct, analyze, and write up rigorous qualitative research with a focus on Glaser's classic grounded theory.

## Setup (Codex CLI)

```bash
./install-codex.sh
```

## Prerequisites

- **Python 3.10+**: For data processing scripts
- **pandoc** (optional): `brew install pandoc` — document conversion
- **Zotero** (optional): Reference management

## Agent Squads

### Methodology Core
| Agent | Role |
|-------|------|
| grounded-theorist | Classic Glaser GT methodology, authoritative guide |
| research-designer | Study design, methodology selection, research questions |
| analysis-orchestrator | Multi-phase analysis pipeline orchestration |
| constant-comparator | Constant comparative method implementation |
| theoretical-sampler | Theoretical sampling decisions |
| literature-integrator | Literature as data, post-emergence integration |

### Coding & Analysis
| Agent | Role |
|-------|------|
| open-coder | Line-by-line open coding, incident-to-incident comparison |
| selective-coder | Core category identification, delimiting theory |
| theoretical-coder | Theoretical coding using Glaser's coding families |
| memo-writer | Theoretical memos, code notes, sorting |
| pattern-analyst | Cross-case patterns, properties, dimensions |
| category-developer | Category development, densification |

### Quality & Rigor
| Agent | Role |
|-------|------|
| saturation-assessor | Theoretical saturation assessment |
| fit-assessor | Fit, work, relevance, modifiability evaluation |
| reflexivity-auditor | Researcher bias, positionality, bracketing |
| methodology-critic | Methodological rigor critique, devil's advocate |
| audit-trail-builder | Decision documentation, transparency |

### Data Work
| Agent | Role |
|-------|------|
| transcript-analyst | Interview transcript analysis and preparation |
| field-note-analyst | Field note processing and organization |
| document-analyst | Document and artifact analysis |
| data-manager | Data organization, storage, retrieval |

### Writing & Output
| Agent | Role |
|-------|------|
| research-writer | Academic findings writing |
| methods-writer | Methodology section writing |
| discussion-writer | Discussion, implications, contributions |
| proposal-writer | Grant and research proposal writing |
| literature-reviewer | Systematic literature review and synthesis |
| citation-manager | Reference formatting (APA 7th, Chicago) |

### Cross-Cutting
| Agent | Role |
|-------|------|
| ethics-reviewer | IRB compliance, informed consent, ethical review |
| peer-reviewer | Simulated peer review, journal-quality feedback |
| planner | Research project planning, timeline, milestones |

## Key Rules

### Glaserian Grounded Theory
Enter the field with an open mind — no preconceived framework, no premature literature review of the substantive area. Let categories emerge from the data through constant comparison. Memo relentlessly. The core category must earn its centrality.

### Rigor Through Transparency
Maintain audit trails. Document every coding decision, category emergence, sampling rationale, and theoretical memo. Trustworthiness comes from methodological transparency, not from checklists applied post hoc.

### All Is Data
Everything is data — interviews, field notes, documents, observations, casual conversations, researcher reflections. Nothing is excluded a priori. Even the literature becomes data once the theory is sufficiently developed.

### No Forcing
Never force data into preexisting categories. Let patterns emerge. If the data doesn't support a category, let it go. GT is about discovery, not verification.

### Ethics First
Every study involving human participants requires IRB approval. Informed consent, confidentiality, data security, and participant wellbeing are non-negotiable. Use pseudonyms. Secure data.

### Academic Writing
Clear, precise, jargon-appropriate prose. APA 7th edition unless otherwise specified. Every claim grounded in data. Theory grounded in evidence.

## Git Conventions
- Commit format: `<type>: <description>`
- Types: feat, fix, refactor, docs, analysis, methodology, ethics, writing
- Keep commits atomic and focused

## Links
- GitHub: https://github.com/ccashwell/qualitative-research-pro
- Glaser, B. G. (1978). *Theoretical Sensitivity*. Sociology Press.
- Glaser, B. G. (1992). *Basics of Grounded Theory Analysis*. Sociology Press.
- Glaser, B. G. (1998). *Doing Grounded Theory: Issues and Discussions*. Sociology Press.
