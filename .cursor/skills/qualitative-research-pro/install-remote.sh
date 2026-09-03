#!/bin/bash
# Qualitative Research Pro remote installer
# Usage: curl -fsSL https://raw.githubusercontent.com/ccashwell/qualitative-research-pro/main/install-remote.sh | bash
set -e

INSTALL_DIR="$HOME/.qualitative-research-pro"
REPO_URL="https://github.com/ccashwell/qualitative-research-pro.git"

echo ""
echo "  Qualitative Research Pro remote installer"
echo "  ================================"
echo ""

if ! command -v git >/dev/null 2>&1; then
  echo "Error: git is required. Install it first."
  exit 1
fi

if ! command -v node >/dev/null 2>&1; then
  echo "Error: Node.js is required. Install it first."
  echo "  https://nodejs.org/"
  exit 1
fi

NODE_VER=$(node -v | sed 's/v//' | cut -d. -f1)
if [ "$NODE_VER" -lt 18 ]; then
  echo "Warning: Node.js >= 18 recommended (you have $(node -v))"
fi

if [ -d "$INSTALL_DIR" ]; then
  echo "Updating existing installation..."
  git -C "$INSTALL_DIR" pull --ff-only 2>/dev/null || {
    echo "Pull failed, re-cloning..."
    rm -rf "$INSTALL_DIR"
    git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"
  }
else
  echo "Cloning Qualitative Research Pro..."
  git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"
fi

echo ""

cd "$INSTALL_DIR"
bash install.sh --non-interactive

echo ""
echo "Done! Qualitative Research Pro is ready."
echo ""
echo "  Agents, skills, hooks, and rules installed."
echo ""
echo "  Academic qualitative research squad installed."
echo ""
echo "github.com/ccashwell/qualitative-research-pro"
echo ""
