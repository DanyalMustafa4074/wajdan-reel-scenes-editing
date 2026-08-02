#!/usr/bin/env bash
# Build one StudyPrime carousel end to end from a spec JSON.
# Usage: bash build.sh <spec.json> <work_dir>
#   <spec.json>  must have hook_image (the chosen Slide-1 PNG) + instagram + linkedin.
# Produces:
#   <work_dir>/slides/slide2..N.png        rendered inner slides
#   <work_dir>/StudyPrime-Carousel-<slug>.pdf   LinkedIn document (all slides)
#   <work_dir>/StudyPrime-Carousel-<slug>.zip   Instagram PNGs + PDF + Captions.txt
set -euo pipefail
SPEC="$1"; WORK="${2:-./carousel-out}"
HERE="$(cd "$(dirname "$0")" && pwd)"
SLIDES="$WORK/slides"
mkdir -p "$SLIDES"

python3 "$HERE/build_html.py" "$SPEC" "$SLIDES"

# Locate a Playwright install and Chromium (works in the CC-web sandbox).
export NODE_PATH="${NODE_PATH:-/opt/node22/lib/node_modules}"
if [ -z "${CHROME:-}" ] && [ -d /opt/pw-browsers ]; then
  CHROME="$(ls /opt/pw-browsers/chromium*/chrome-linux/chrome 2>/dev/null | grep -v headless | head -1 || true)"
  export CHROME
fi
node "$HERE/render.js" "$SLIDES"

python3 "$HERE/pack.py" "$SPEC" "$SLIDES" "$WORK"
echo "DONE -> $WORK"
