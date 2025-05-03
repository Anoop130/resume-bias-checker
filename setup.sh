#!/usr/bin/env bash
set -euo pipefail

# 1. Create venv (if it doesn't already exist)
if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo "Created virtualenv in ./venv"
fi

# 2. Activate it
#    Note: if you're on Windows, use: source venv/Scripts/activate
source venv/bin/activate

# 3. Upgrade pip
pip install --upgrade pip

# 4. Install dependencies
pip install \
  python-dotenv \
  pandas \
  PyPDF2 \
  langchain \
  langchain_openai \
  openai

echo
echo "✅ All dependencies installed!"
echo "   To start working, run:  source venv/bin/activate"
