#!/bin/bash
# Qualitative Research Pro installer for Cursor IDE
# Copies skills to project and sets up .cursor/rules

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="${1:-.}"
ADDED=0
SKIPPED=0

echo "Qualitative Research Pro installer for Cursor IDE"
echo "========================================="
echo ""
echo "Target project: $(cd "$TARGET_DIR" && pwd)"
echo ""
echo "This will install:"
echo "  - .cursor/rules/*.mdc  (6 rule files)"
echo "  - AGENTS.md            (project instructions)"
echo ""

read -p "Continue? (y/N) " -n 1 -r
echo
[[ $REPLY =~ ^[Yy]$ ]] || exit 0

mkdir -p "$TARGET_DIR/.cursor/rules"

for f in "$REPO_DIR/.cursor/rules/"*.mdc; do
  [ -f "$f" ] || continue
  name=$(basename "$f")
  if [ ! -e "$TARGET_DIR/.cursor/rules/$name" ]; then
    cp "$f" "$TARGET_DIR/.cursor/rules/$name"
    ADDED=$((ADDED + 1))
  else
    SKIPPED=$((SKIPPED + 1))
  fi
done

if [ ! -e "$TARGET_DIR/AGENTS.md" ]; then
  cp "$REPO_DIR/AGENTS.md" "$TARGET_DIR/AGENTS.md"
  ADDED=$((ADDED + 1))
else
  SKIPPED=$((SKIPPED + 1))
fi

echo ""
echo "Installation complete!"
echo "  Added:   $ADDED files"
echo "  Skipped: $SKIPPED files (already existed)"
echo ""
echo "Cursor will now use Qualitative Research Pro rules for this project."
