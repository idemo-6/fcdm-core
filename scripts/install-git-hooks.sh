#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
hooks_path="$repo_root/.githooks"

if [[ ! -d "$hooks_path" ]]; then
  echo "Hooks directory not found: $hooks_path" >&2
  exit 1
fi

chmod +x "$hooks_path/pre-commit" "$hooks_path/commit-msg" "$hooks_path/pre-push"
git -C "$repo_root" config core.hooksPath .githooks

if ! python3 -c "import yaml" >/dev/null 2>&1; then
  echo "Missing dependency: PyYAML"
  echo "Install it with: python3 -m pip install --user PyYAML"
  exit 1
fi

echo "Installed git hooks via core.hooksPath=.githooks"
echo "Hooks:"
echo "  - pre-commit"
echo "  - commit-msg"
echo "  - pre-push"
