# Scholarly

> An AI agent skill that guides you through writing academic papers and theses, section by section.

![Skill Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-OpenClaw%20%7C%20Claude%20Code%20%7C%20Cursor%20%7C%20通用Agent-blue)

## What is Scholarly?

Scholarly is an AI-powered academic writing assistant that helps researchers, graduate students, and academics build complete research papers through guided conversation.

Instead of staring at a blank document, Scholarly guides you through a series of targeted questions to progressively develop each section of your paper—from Abstract to Introduction, Literature Review, Methods, Results, Discussion, and Conclusion.

## Features

### 🎯 Guided Section-by-Section Development
- Start with Title & Abstract
- Build Introduction through progressive context-setting
- Conduct systematic Literature Review with gap identification
- Detail Methods for full reproducibility
- Report Results with proper statistical formatting
- Discuss findings with theoretical and practical implications
- Conclude with clear takeaways

### 📚 Comprehensive Writing Guidance
- Section-specific structures and templates
- Common mistakes to avoid
- Statistical reporting formats (APA style)
- Sentence starters and transition phrases
- Discipline-specific considerations

### 📖 11 Core Sections Covered
| Section | What's Covered |
|---------|----------------|
| Title | Keywords, conciseness, variable naming |
| Abstract | 250-word structure, past/present tense |
| Introduction | 4-layer structure (Context → Lit → Gap → Purpose) |
| Literature Review | Thematic/chonological/methodological organization |
| Methods | Participants, design, materials, procedure, analysis |
| Results | Statistical reporting, tables vs. figures |
| Discussion | Interpretation, literature dialogue, limitations |
| Conclusion | Key takeaways, avoiding redundancy |
| References | APA 7th format quick reference |
| Thesis-specific | Bachelor's, Master's, PhD requirements |

### 📋 Templates Included
- Abstract template (250 words)
- Introduction outline
- Methods sub-structure
- Discussion structure
- Statistical notation guide

## Platform Compatibility

Scholarly works with any AI agent framework that supports skills:

- **OpenClaw / WorkBuddy** — Install to `~/.workbuddy/skills/`
- **Claude Code** — Install to `~/.claude/skills/`
- **Cursor** — Install to `~/.cursor/skills/`
- **Other frameworks** — Any agent that reads `SKILL.md` from a skills directory

## Installation

### For OpenClaw / WorkBuddy Users
```bash
cp -r scholarly ~/.workbuddy/skills/
```
Restart your agent to activate.

### For Claude Code Users
```bash
cp -r scholarly ~/.claude/skills/
```

### For Cursor Users
```bash
cp -r scholarly ~/.cursor/skills/
```

### For Developers
```bash
git clone https://github.com/ShiyangZheng/scholarly.git
```

## Usage

### In Conversation
Simply tell the agent what you're working on:

> "I'm writing my psychology undergraduate thesis on the relationship between social media use and anxiety."

> "Help me outline a literature review on machine learning in education."

> "I'm preparing a methods section for my mixed-methods dissertation on ESL learners."

### The Process

1. **Foundation**: Scholarly asks about your paper type, discipline, research design, and citation style.

2. **Section-by-Section**: Each section is developed through targeted questions:
   - What are your key variables?
   - What's your target sample?
   - What are your main hypotheses?

3. **Draft Generation**: Complete section drafts with templates and examples.

4. **Iteration**: Refine each section based on your feedback.

### Paper Types Supported

| Type | Description |
|------|-------------|
| Course Paper | Undergraduate/graduate coursework papers |
| Journal Article | Peer-reviewed publications |
| Conference Paper | Academic conference submissions |
| Bachelor's Thesis | Undergraduate honors thesis |
| Master's Thesis | Graduate thesis |
| Doctoral Dissertation | PhD dissertation |
| Literature Review | Standalone review articles |

### Research Designs Supported

- **Quantitative**: Experiments, surveys, correlational studies
- **Qualitative**: Interviews, ethnography, case studies
- **Mixed Methods**: Combining quantitative and qualitative approaches
- **Systematic Review**: PRISMA-style comprehensive reviews

## File Structure

```
scholarly/
├── README.md                              # This file
├── SKILL.md                               # Skill definition (universal agent framework)
└── references/
    └── academic_paper_templates.md         # Detailed templates for all sections
```

## Citation Format Support

- APA 7th Edition
- MLA
- Chicago
- Harvard
- IEEE
- Vancouver

(Reference formatting guides included in `references/`)

## Contributing

Contributions welcome! Feel free to:
- Add discipline-specific templates (e.g., for chemistry, law, medicine)
- Improve section templates
- Add language-specific guides
- Report issues or suggestions

## Resources

Based on best practices from:
- APA Publication Manual (7th Edition)
- Purdue OWL (Online Writing Lab)
- UNC Writing Center
- UCSD Psychology Writing Resources

## License

MIT License - Free to use, modify, and distribute.

---

*Scholarly—where research takes shape.*
