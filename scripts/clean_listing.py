#!/usr/bin/env python3
"""Преобразование OCR-текста листинга МАДЛЕН в исходник.

Убирает колонки листинга (номера строк, адреса, счётчики ошибок),
оставляя метку, операцию, операнды и комментарий.

Формат строки листинга (примеры):
    DOG00110 PROGRAM : , NAME,
    DOG003530        , XTA , F START .ТАКТИРОВ.РЕЖИМ
    0134 0061 DOG003530 ...
    DOG00350C------- ..........
"""
import re
import sys

# Метка листинга: 2-8 букв + 5 цифр + необязательный признак строки (0/C/-)
LABEL = re.compile(r"(?<![A-Za-z0-9])([A-ZА-ЯЁ]{2,8}\d{5})([0-9Cc\-]?)")


def clean_line(line: str) -> str | None:
    s = line.rstrip("\n\r").replace("\x0c", "")
    m = LABEL.search(s)
    if not m:
        return None
    flag = m.group(2)
    rest = s[m.end():].strip()
    # Разделители-линии комментариев и мусор OCR
    if not rest:
        return None
    if flag in ("C", "c", "-") or rest.startswith(("---", "===", "***")):
        return "С" + (" " + rest.lstrip("C- ") if rest.strip("C- ") else "")
    # Иногда OCR относит признак C к следующей строке
    if rest.startswith("C ") or rest.startswith("C---"):
        return "С " + rest[1:].lstrip("- ")
    return rest


def clean(text: str) -> str:
    out = []
    for line in text.splitlines():
        if line.startswith("=== PAGE"):
            out.append(line)
            continue
        c = clean_line(line)
        if c is not None:
            out.append(c)
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    data = open(sys.argv[1], encoding="utf-8", errors="replace").read()
    sys.stdout.write(clean(data))
