#!/bin/bash

# Auto commit message or default one
MSG=${1:-"update"}

# Add all changes
git add .

# Commit only if there are changes
if git diff --cached --quiet; then
  echo "No changes to commit."
else
  git commit -m "$MSG"
fi

# Push current branch
git push origin $(git rev-parse --abbrev-ref HEAD)
