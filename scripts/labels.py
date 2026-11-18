#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Извлечение меток вида <префикс><4-6 цифр> по страницам; кластеризация префиксов."""
import re
from collections import Counter, defaultdict

BASE = "/tmp/.private/azizz/opencode/glissada"
pages = {}
for i in range(1, 336):
    pages[i] = open(f"{BASE}/ocr/p{i:03d}.txt", encoding='utf-8', errors='replace').read()

LAB = re.compile(r'(?<![A-Za-zА-Яа-яЁё0-9])([A-Za-zА-Яа-яЁё]{2,5})\s?(\d{4,6}[A-Za-zА-Яа-яЁё]?)')
TR = str.maketrans({'А':'A','В':'B','Е':'E','К':'K','М':'M','Н':'H','О':'O','Р':'P','С':'C',
    'Т':'T','Х':'X','У':'Y','И':'N','Г':'F','Д':'D','Л':'L','П':'P','Ф':'Q','Я':'R',
    'Ш':'W','Щ':'W','З':'3','Й':'N','Ё':'E','Б':'B','Ю':'O','Ж':'X','Ц':'U',
    '0':'O','1':'I','8':'B','6':'G','9':'g','5':'S','3':'E','2':'Z'})
norm = lambda s: s.translate(TR).upper()

# Кластеры: каноническое имя -> набор нормализованных префиксов
CLUSTERS = {
 'DOG': {'DOG','DOO','DOGO','006','206','00G','DO6','206G','D0G','D06','D8G'},
 'MRV': {'MRV','MRY','MRVO','MPY','MKY','MAV','MYV','MRQ','MRU','M8V','MRB','MBV'},
 'REA': {'REA','REAI','REAO','REAQ','BEA','BEAO','BEO','HEA','REI','RE1','PEA','LEA'},
 'WRI': {'WRI','WRY','WRR','WRIO','WRT','WOP','WEP','WED','WR','W1','WKI'},
 'RCD': {'RCD','RCP','RCH','RCO','RCE','REB','RCR','RCA','KCD','RCDO'},
 'WCD': {'WCD','WOD','WED','WCO','W0D','MCD','M0D','WCDO'},
 'M7B': {'M7B','N7B','M?B','N?B','MZB','M7R','N7R'},
 'PS':  {'PS','P5','PZ','PY','P'} ,
 'DEB': {'DEB','DER','DE8','DE6','DE0','D8B','DEBO','PEB','BEB','REB','pEB'},
}
def cluster(pre):
    for c, s in CLUSTERS.items():
        if pre in s:
            return c
    return None

prof = {}
for p, text in pages.items():
    c = Counter()
    lablist = []
    for line in text.splitlines():
        for m in LAB.finditer(line):
            pre = norm(m.group(1))
            cl = cluster(pre)
            if cl:
                c[cl] += 1
                lablist.append((cl, m.group(1)+m.group(2)))
    prof[p] = (c, lablist)

print("=== PAGE PROFILE: dominant cluster, counts, first/last label ===")
for p in sorted(prof):
    c, labs = prof[p]
    if not labs:
        print(f"{p:3d}: --- (no labels)")
        continue
    top = c.most_common(3)
    s = f"{p:3d}: " + ", ".join(f"{k}={v}" for k,v in top)
    s += f" | first={labs[0][1]} last={labs[-1][1]}"
    print(s)
