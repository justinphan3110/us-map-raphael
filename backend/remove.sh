#!/bin/bash

git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch backend/weather.key" \
  --prune-empty --tag-name-filter cat -- --all