#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
INPUT="${1:-$ROOT_DIR/proposal.md}"
OUTPUT="${2:-$ROOT_DIR/output/Rode_Banff_Proposal_from_md.pdf}"
CSS="${3:-$ROOT_DIR/portfolio-docs.css}"

mkdir -p "$(dirname "$OUTPUT")"

pandoc \
  "$INPUT" \
  --from=gfm \
  --standalone \
  --css "$CSS" \
  --pdf-engine=weasyprint \
  --output "$OUTPUT"

echo "Generated: $OUTPUT"
