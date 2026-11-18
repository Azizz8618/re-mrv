#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Анализ OCR-текста: префиксы меток, директивы, заголовки по страницам."""
import re, os, glob
from collections import Counter, defaultdict

BASE = "/tmp/.private/azizz/opencode/glissada"
pages = {}
for i in range(1, 336):
    f = f"{BASE}/ocr/p{i:03d}.txt"
    with open(f, encoding='utf-8', errors='replace') as fh:
        pages[i] = fh.read()

# Нормализация «похожих» символов (кириллица -> латиница, цифры -> буквы)
TR = str.maketrans({
    'А':'A','а':'A','В':'B','в':'B','Е':'E','е':'E','К':'K','к':'K','М':'M','м':'M',
    'Н':'H','н':'H','О':'O','о':'O','Р':'P','р':'P','С':'C','с':'C','Т':'T','т':'T',
    'Х':'X','х':'X','У':'Y','у':'Y','И':'N','и':'N','Г':'F','г':'F','Д':'D','д':'D',
    'Л':'L','л':'L','П':'P','п':'P','Ф':'Q','ф':'Q','Я':'R','я':'R','Ч':'4','ч':'4',
    'Ш':'W','ш':'W','Щ':'W','щ':'W','З':'3','з':'3','Й':'N','й':'N','Ё':'E','ё':'E',
    'Б':'B','б':'B','Ю':'O','ю':'O','Ж':'X','ж':'X','Ц':'U','ц':'U',
    '0':'O','1':'I','8':'B','6':'G','9':'g','5':'S','3':'E','7':'7','2':'Z','4':'4',
})
def norm(s):
    return s.translate(TR).upper()

# Метка: в начале строки (после пробелов) 3-4 буквы + 3+ цифр, опц. буква/C в конце
LABEL_RE = re.compile(r'(?<![A-Za-zА-Яа-яЁё0-9])([A-Za-zА-Яа-яЁё]{3,5})\s?(\d{3,7}[A-Za-zА-Яа-яЁё]?)')

prefix_by_page = defaultdict(Counter)
for p, text in pages.items():
    for line in text.splitlines():
        for m in LABEL_RE.finditer(line):
            pre = norm(m.group(1))
            if len(pre) >= 3:
                prefix_by_page[p][pre] += 1

# Глобальные частоты префиксов
total = Counter()
for c in prefix_by_page.values():
    total.update(c)
print("=== TOP PREFIXES (normalized) ===")
for pre, n in total.most_common(40):
    print(f"{pre:6s} {n}")

print()
print("=== DOMINANT PREFIX PER PAGE ===")
for p in sorted(pages):
    c = prefix_by_page[p]
    if not c:
        print(f"{p:3d}: ---")
        continue
    top = c.most_common(3)
    print(f"{p:3d}: " + ", ".join(f"{k}:{v}" for k, v in top))
