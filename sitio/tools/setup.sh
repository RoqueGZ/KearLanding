#!/usr/bin/env bash
set -euo pipefail
site_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$site_root"
mkdir -p .local/bootstrap .local/runtime
npm --cache "$site_root/.local/npm-cache" install --prefix "$site_root/.local/bootstrap" --no-audit --no-fund npm@11.16.0
cp tools/package.json tools/package-lock.json .local/runtime/
node .local/bootstrap/node_modules/npm/bin/npm-cli.js --cache "$site_root/.local/npm-cache" ci --prefix "$site_root/.local/runtime" --no-audit --no-fund --ignore-scripts
if [[ ! -f .local/WordPress-6.8/wp-load.php ]]; then
  curl -fL --silent --show-error --max-time 120 https://github.com/WordPress/WordPress/archive/refs/tags/6.8.zip -o .local/wordpress-6.8.zip
  python3 - <<'PY'
from zipfile import ZipFile
with ZipFile('.local/wordpress-6.8.zip') as archive:
    assert archive.testzip() is None, 'Corrupt WordPress archive'
    archive.extractall('.local')
PY
fi
python3 tools/preview.py
