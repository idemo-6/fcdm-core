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

echo "Installed git hooks via core.hooksPath=.githooks"
echo "Hooks:"
echo "  - pre-commit"
echo "  - commit-msg"
echo "  - pre-push"
