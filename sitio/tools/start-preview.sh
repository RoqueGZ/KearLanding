#!/usr/bin/env bash
set -euo pipefail
site_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$site_root/tools/preview.py"
exec python3 -m http.server 4173 --bind 127.0.0.1 --directory "$site_root"
