#!/usr/bin/env bash
set -euo pipefail

# Directory containing your .docx files
DIR="resumes"

# 1) Check that the directory exists
if [ ! -d "$DIR" ]; then
  echo "Directory '$DIR' not found." >&2
  exit 1
fi

# 2) Check that LibreOffice is installed
if ! command -v libreoffice &> /dev/null; then
  echo "LibreOffice not found. Please install it (e.g. sudo apt install libreoffice)." >&2
  exit 1
fi

# 3) Loop over each .docx file and convert
shopt -s nullglob
for docx in "$DIR"/*.docx; do
  outdir="$(dirname "$docx")"
  base="$(basename "${docx%.docx}")"
  pdf="$outdir/$base.pdf"

  echo "Converting '$docx' → '$pdf'..."
  libreoffice --headless --convert-to pdf "$docx" --outdir "$outdir"
done

echo "✅ All .docx files in '$DIR' have been converted to PDF."
