#!/bin/bash
# build2.sh <source.txt> <name> — компиляция без запуска программы
set -u
SRC="$1"
NAME="${2:-DOG2FIX}"
B6="${SRC%.txt}.b6"
LST="${SRC%.txt}.lst"
python3 - "$SRC" "$NAME" "$B6" << 'PYEOF'
import sys
src, name, b6 = sys.argv[1], sys.argv[2], sys.argv[3]
header = [
    'шифр 419999 зс5^',
    'лен 41(2048)^',
    'eeв1а3',
    f'*name {name}',
    '*no list',
    '*assembler',
]
footer = ['*end file', '``````', 'еконец']
with open(src, 'r', encoding='utf-8') as f:
    lines = f.readlines()
out = []
for line in lines:
    raw = line.rstrip('\n')
    stripped = raw.strip()
    if stripped.startswith('.'):
        t = stripped[1:].lstrip()
        out.append('С ' + t if t else 'С')
        continue
    out.append(raw)
with open(b6, 'w', encoding='utf-8') as f:
    for line in header + out + footer:
        f.write(line + '\n')
print(f'{name}: {len(out)} строк -> {b6}')
PYEOF
timeout 25 dispak "$B6" > "$LST" 2>&1
echo "Ошибок (**): $(grep -o '\*\*\*\*\*\*' "$LST" | wc -l)"
python3 - "$LST" <<'PY'
import re,sys
txt=open(sys.argv[1],encoding='utf-8').read()
syms=re.findall(r'НЕОПИСАННЫЙ ИДЕНТИФИКАТОР\s+(\S+)',txt)
oth=[m.strip() for m in re.findall(r'\*\*\*\*\*\*([^*]+)',txt) if 'НЕОПИСАННЫЙ' not in m]
from collections import Counter
print('Неописанные:', dict(Counter(syms)))
print('Другие:', dict(Counter(oth)))
print('Конец листинга:', 'ОЧЕНЬ МНОГО ОШИБОК' in txt)
PY
