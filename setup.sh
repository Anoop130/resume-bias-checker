#!/usr/bin/env bash
set -euo pipefail

# 0) Ensure LibreOffice
command -v libreoffice &>/dev/null || {
  echo "Installing LibreOffice…"
  sudo apt-get update && sudo apt-get install -y libreoffice
}

# 1) venv
[ -d venv ] || python3 -m venv venv
source venv/bin/activate

# 2) pip
pip install --upgrade pip

# 3) deps (pin as needed)
pip install \
  python-dotenv \
  PyPDF2 \
  langchain \
  groq

echo "Dependencies ready — activate with: source venv/bin/activate"
