#!/bin/bash
# check_all.sh — проверить все расшифрованные модули репозитория.
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"
mkdir -p build/check
fail=0
while IFS= read -r src; do
    name=$(basename "$(dirname "$src")")
    if ! bash scripts/build_one.sh "$src" "$name" build/check; then
        fail=$((fail+1))
    fi
done < <(find docs -mindepth 2 -maxdepth 2 -name '*_src.txt' | sort)
echo "---"
echo "Источников с ошибками: $fail"
exit $fail
