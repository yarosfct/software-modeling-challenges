# Contributing to Qualitative Research Pro

Thanks for considering contributing! Here's how you can help build the qualitative research squad.

## Ways to Contribute

### Add New Agents

Create a `.md` file in `agents/` with YAML frontmatter:

```yaml
---
name: my-agent
description: "What this agent does — one clear sentence"
model: sonnet
tools: [Read, Write, Edit, Bash, Grep, Glob]
---

Your agent prompt here. Be specific about the research methodology role,
expertise areas, procedures, and output format.
```

**Fields:**
- `name` (required): kebab-case identifier
- `description` (required): role description
- `model` (optional): `opus` (complex reasoning) or `sonnet` (fast execution). Default: sonnet
- `tools` (optional): subset of Read, Write, Edit, Bash, Grep, Glob, Task

### Add New Skills

Create a directory in `skills/` with a `SKILL.md`:

```yaml
---
name: my-skill
description: "When to use this skill and what methodology knowledge it provides"
---

Skill content — methodology procedures, analytical techniques,
key references, templates, checklists, common pitfalls.
```

**Fields:**
- `name` (required): kebab-case identifier
- `description` (required): what this skill covers and when to use it

**Quality requirements:**
- All methodology claims must cite primary sources (author, year)
- Distinguish between GT traditions when discussing grounded theory
- Include worked examples showing how techniques apply to data
- Key references must be real, published works — never hallucinated

### Improve Hooks

TypeScript hooks live in `hooks/src/`. Each hook is a separate ESM module.

**Development workflow:**

```bash
cd hooks
npm install          # install dev dependencies
npm run build        # compile TypeScript to dist/*.mjs
npm test             # run unit tests
npm run test:watch   # watch mode
```

### Add New Rules

Create a `.md` file in `rules/` for research methodology guidelines:

```markdown
# Rule Name

## When to Apply
Describe when this rule is relevant.

## Guidelines
Specific, actionable rules with methodology examples.

## Checklist
- [ ] Concrete items to verify
```

### Testing

```bash
cd hooks
npm test                    # run all tests
npm run test:watch          # watch mode
npm run check               # TypeScript type check
```

### Documentation

- Improve agent/skill content with deeper methodology knowledge
- Add worked examples demonstrating analytical techniques
- Add key references from the qualitative methods literature
- See [ARCHITECTURE.md](ARCHITECTURE.md) for system design overview

### Bug Reports & Feature Requests

Open an issue using the provided templates. Include your OS and Node.js version.

## Development Setup

```bash
git clone https://github.com/ccashwell/qualitative-research-pro.git
cd qualitative-research-pro
./install.sh
```

### Prerequisites

- **Python 3.10+**: For data processing utilities
- **Node.js** >= 18 (for hook compilation)
- **pandoc** (optional): `brew install pandoc`

## Pull Request Process

1. Fork the repo
2. Create a feature branch (`git checkout -b feat/my-new-agent`)
3. Write tests for hook changes
4. Commit with clear messages (`feat:`, `fix:`, `docs:`, `methodology:`, etc.)
5. Push and open a PR against `main`
6. Describe what you added and why
7. CI will validate frontmatter, lint markdown, and run tests

## Code Style

- **Agents**: Markdown + YAML frontmatter. Research methodology expertise.
- **Skills**: Markdown (`SKILL.md`) + YAML frontmatter. Methodology knowledge with primary source citations.
- **Hooks**: TypeScript (ES2022, NodeNext modules), built with esbuild.
- **Rules**: Markdown. Research methodology guidelines.
- **Methodology claims**: Must cite primary sources. Distinguish GT traditions clearly.

## Good First Issues

Look for issues labeled `good first issue`:
- Add a missing agent for a specific qualitative methodology
- Improve a skill with deeper methodology knowledge or more examples
- Add key references from the qualitative methods literature
- Add test coverage for a hook utility
- Improve methodology examples in existing skills

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
