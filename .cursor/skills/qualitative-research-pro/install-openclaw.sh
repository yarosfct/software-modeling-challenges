#!/bin/bash
# Qualitative Research Pro installer for OpenClaw
# Copies skills to ~/.openclaw/skills/ (shared across all agents)
# and sets up workspace bootstrap files
#
# Usage: ./install-openclaw.sh [--force] [--workspace-only] [--skills-only]

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
OPENCLAW_DIR="$HOME/.openclaw"
WORKSPACE_DIR="$OPENCLAW_DIR/workspace"
FORCE=false
SKILLS_ONLY=false
WORKSPACE_ONLY=false
ADDED=0
SKIPPED=0

for arg in "$@"; do
  case $arg in
    --force) FORCE=true ;;
    --skills-only) SKILLS_ONLY=true ;;
    --workspace-only) WORKSPACE_ONLY=true ;;
    --help|-h)
      echo "Usage: ./install-openclaw.sh [--force] [--skills-only] [--workspace-only]"
      echo ""
      echo "  --force           Overwrite existing files (default: skip existing)"
      echo "  --skills-only     Only install skills to ~/.openclaw/skills/"
      echo "  --workspace-only  Only install workspace bootstrap files"
      echo ""
      echo "Installs Qualitative Research Pro skills and workspace config for OpenClaw."
      exit 0
      ;;
  esac
done

echo "Qualitative Research Pro installer for OpenClaw"
echo "======================================="
echo ""

if command -v openclaw &> /dev/null; then
  echo "OpenClaw: found"
else
  echo "Warning: openclaw command not found."
  echo "  Install: https://docs.openclaw.ai/install"
  echo ""
  echo "Continuing with file installation anyway..."
fi
echo ""

SKILL_COUNT=$(find "$REPO_DIR/skills/" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')

if [ "$WORKSPACE_ONLY" != true ]; then
  echo "This will install:"
  echo "  - $SKILL_COUNT skills -> ~/.openclaw/skills/"
fi
if [ "$SKILLS_ONLY" != true ]; then
  echo "  - AGENTS.md   -> ~/.openclaw/workspace/"
  echo "  - TOOLS.md    -> ~/.openclaw/workspace/"
fi
echo ""

if [ "$FORCE" = true ]; then
  echo "Mode: OVERWRITE (--force)"
else
  echo "Mode: MERGE (default) — existing files preserved"
fi
echo ""

if command -v python3 &>/dev/null; then
  echo "Python detected: $(python3 --version 2>/dev/null)"
else
  echo "NOTE: Python 3 not found. Recommended for data processing."
fi
echo ""

read -p "Continue? (y/N) " -n 1 -r
echo
[[ $REPLY =~ ^[Yy]$ ]] || exit 0

smart_copy_file() {
  local src="$1"
  local dest="$2"
  if [ "$FORCE" = true ] || [ ! -e "$dest" ]; then
    cp "$src" "$dest"
    ADDED=$((ADDED + 1))
  else
    SKIPPED=$((SKIPPED + 1))
  fi
}

smart_copy_dir() {
  local src="$1"
  local dest="$2"
  if [ "$FORCE" = true ] || [ ! -e "$dest" ]; then
    cp -r "$src" "$dest"
    ADDED=$((ADDED + 1))
  else
    SKIPPED=$((SKIPPED + 1))
  fi
}

if [ "$WORKSPACE_ONLY" != true ]; then
  echo "Installing skills..."
  mkdir -p "$OPENCLAW_DIR/skills"
  for d in "$REPO_DIR/skills/"*/; do
    name=$(basename "$d")
    [ "$name" = "*" ] && continue
    smart_copy_dir "$d" "$OPENCLAW_DIR/skills/$name"
  done
fi

if [ "$SKILLS_ONLY" != true ]; then
  echo "Installing workspace files..."
  mkdir -p "$WORKSPACE_DIR"

  smart_copy_file "$REPO_DIR/AGENTS.md" "$WORKSPACE_DIR/AGENTS.md"

  if [ ! -e "$WORKSPACE_DIR/TOOLS.md" ]; then
    cat > "$WORKSPACE_DIR/TOOLS.md" << 'TOOLSEOF'
# Tools — Qualitative Research Pro

## Recommended Software

- **Python 3.10+** — Data processing, scripting
- **pandoc** — Document conversion (brew install pandoc)
- **Zotero** — Reference management

## CAQDAS Options

- NVivo 15 — Full-featured qualitative analysis
- ATLAS.ti 24 — Visual coding and analysis
- MAXQDA 2024 — Mixed methods support
- Dedoose — Cloud-based, collaborative

## Conventions

- Default to Glaser's classic grounded theory
- APA 7th edition for citations unless otherwise specified
- Pseudonyms for all participants, always
- Never commit identifiable participant data
TOOLSEOF
    ADDED=$((ADDED + 1))
  else
    SKIPPED=$((SKIPPED + 1))
  fi
fi

INSTALLED_SKILLS=$(find "$OPENCLAW_DIR/skills/" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')

echo ""
echo "Installation complete!"
echo "  Added:   $ADDED files"
echo "  Skipped: $SKIPPED files (already existed)"
echo ""
if [ "$WORKSPACE_ONLY" != true ]; then
  echo "  Skills in ~/.openclaw/skills/: $INSTALLED_SKILLS"
fi
if [ "$SKILLS_ONLY" != true ]; then
  echo "  Workspace: $WORKSPACE_DIR"
fi
echo ""
if [ $SKIPPED -gt 0 ]; then
  echo "Tip: Use ./install-openclaw.sh --force to overwrite existing files."
  echo ""
fi
echo "Usage:"
echo "  openclaw agent --message \"help me with open coding on this transcript\""
echo "  openclaw agent --message \"use the glaserian-grounded-theory skill\""
echo ""
