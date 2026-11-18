#!/bin/bash
# build_one.sh — сборка одного МАДЛЕН-исходника через dispak.
# Использование: build_one.sh <source.txt> <module-name> <output-dir>
# Исходник НЕ изменяется: .b6 и листинг создаются в <output-dir>.
set -e
SRC="$1"; NAME="$2"; OUT="${3:-build}"
mkdir -p "$OUT"
BASE=$(basename "$SRC" .txt)
B6="$OUT/${BASE}.b6"

python3 - "$SRC" "$NAME" "$B6" <<'PY'
import sys
src, name, b6 = sys.argv[1], sys.argv[2], sys.argv[3]
header = ['шифр 419999 зс5^', 'лен 41(2048)^', 'eeв1а3',
          f'*name {name}', '*no list', '*assembler']
footer = ['*execute', '*end file', '``````', 'еконец']
with open(src, encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f]
# Строки-комментарии, начинающиеся с '.', конвертируем в 'С' (требование МАДЛЕН)
lines = [('С' + l.lstrip()[1:]) if l.lstrip().startswith('.') else l for l in lines]
with open(b6, 'w', encoding='utf-8') as f:
    f.write('\n'.join(header + lines + footer) + '\n')
PY

(cd "$OUT" && dispak "$(basename "$B6")" > "${BASE}.lst" 2>&1)
if grep -q "БЫЛИ ОШИБКИ\|ОЧЕНЬ МНОГО ОШИБОК\|НЕДОПУСТИМЫЙ\|НЕОПИСАННЫЙ\|ДВАЖДЫ ОПИСАННЫЙ\|ОШИБКА В КОП" "$OUT/${BASE}.lst"; then
    echo "FAIL $SRC — ошибки трансляции (см. $OUT/${BASE}.lst)"
    exit 1
fi
echo "OK   $SRC -> $OUT/${BASE}.lst"
