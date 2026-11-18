#!/bin/bash
# check_all.sh — проверить все компилируемые исходники из docs/SOURCES.txt.
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"
mkdir -p build/check
fail=0
total=0
while IFS= read -r src; do
    case "$src" in ''|\#*) continue;; esac
    if [ ! -f "$src" ]; then
        echo "MISS $src"
        fail=$((fail+1))
        continue
    fi
    total=$((total+1))
    name=$(basename "$(dirname "$src")")
    if ! bash scripts/build_one.sh "$src" "$name" build/check; then
        fail=$((fail+1))
    fi
done < docs/SOURCES.txt
echo "---"
echo "Проверено: $total; с ошибками: $fail"
exit $fail
