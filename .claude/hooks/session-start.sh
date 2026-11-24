#!/bin/bash
# At every session start, fetch the latest state from GitHub and print a
# summary. A SessionStart hook's stdout is added to Claude's context.
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

# Fetch all branches; a network failure must not block the session.
timeout 30 git fetch --all --prune --quiet 2>/dev/null || echo "(git fetch failed; showing local state)"

branch=$(git branch --show-current 2>/dev/null)
default=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null || echo origin/main)

echo "=== GitHub context for $(git remote get-url origin 2>/dev/null) ==="
echo "Current branch: ${branch:-detached}   Default branch: $default"

if [ -n "$branch" ] && git rev-parse --verify --quiet "origin/$branch" >/dev/null; then
  read -r ahead behind < <(git rev-list --left-right --count "$branch...origin/$branch")
  echo "vs origin/$branch: $ahead ahead, $behind behind"
fi
if [ -n "$branch" ]; then
  read -r ahead behind < <(git rev-list --left-right --count "$branch...$default")
  echo "vs $default: $ahead ahead, $behind behind"
fi

echo
echo "--- Recent commits on $default ---"
git log "$default" --oneline -15 2>/dev/null

echo
echo "--- Remote branches (newest first) ---"
git for-each-ref --sort=-committerdate --count=15 \
  --format='%(refname:short)  %(committerdate:short)  %(subject)' refs/remotes/origin \
  | grep -v '^origin/HEAD'

echo
echo "--- Uncommitted changes ---"
git status --short | head -30
[ -z "$(git status --short)" ] && echo "(none)"

# Show these files as they are on the default branch, not the local copy.
for f in CLAUDE.md README.md; do
  if git cat-file -e "$default:$f" 2>/dev/null; then
    echo
    echo "--- $f (from $default) ---"
    git show "$default:$f" | head -100
  fi
done

exit 0
