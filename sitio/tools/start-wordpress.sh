#!/usr/bin/env bash
set -euo pipefail
site_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
exec "$site_root/.local/runtime/node_modules/.bin/wp-playground-cli" server \
  --mount-before-install "$site_root/.local/WordPress-6.8:/wordpress" \
  --mount "$site_root/kear-landings:/wordpress/wp-content/themes/kear-landings" \
  --wordpress-install-mode install-from-existing-files-if-needed \
  --wp 6.8 --php 8.3 --port 9400 --workers 6 \
  --blueprint "$site_root/tools/wordpress-blueprint.json"
